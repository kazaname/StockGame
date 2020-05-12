from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView
from .forms import WalletModelForm, PurchasedShareModelForm
from .models import Wallet, PurchasedShare
# from rest_framework import viewsets
# from .serializers import WalletSerializer, PurchasedShareSerializer


class WalletsListView(ListView):
    queryset = Wallet.objects.filter(is_private=False)
    template_name = "stock_wallet/wallets_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(WalletsListView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            private_wallets = Wallet.objects.filter(user=self.request.user ,is_private=True)
        else:
            private_wallets = None
        context['private_wallets'] = private_wallets
        return context
    # Szkolenie eCommerce
    # def get_context_data(self, *args, **kwargs):
    #     context = super(PublicWalletsListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # Moja twórczość
    # def get_queryset(self):
    #     return Wallet.objects.filter(is_private=False)

class WalletsDetailView(DetailView):
    model = Wallet
    template_name = "stock_wallet/wallet_detail.html"

    # Poniższa metoda pozwala na wyciągnięcie z kwargs wartości id i pobranie objektu o podanym numerze id
    # def get_object(self):
    #     id_ = self.kwargs.get('id')
    #     return get_object_or_404(Wallet, id=id_)

    def get_object(self):
        object = get_object_or_404(Wallet, slug=self.kwargs.get('slug'))
        if object.is_private == True:
            if object.user == self.request.user:
                return object
            else:
                raise PermissionDenied
        else:
            return object

    def get_context_data(self, *args, **kwargs):
        context = super(WalletsDetailView, self).get_context_data(*args, **kwargs)
        qs_shares = context['object'].purchasedshare_set.distinct('company_name')
        context['shares'] = {}
        for qs in qs_shares:
            context['shares'][qs.company_name] = {}
            sum_dict = {}
            amount = 0
            qs_company = context['object'].purchasedshare_set.filter(company_name=qs.company_name, status=True)
            context['shares'][qs.company_name]['data'] = qs_company
            price_per_one = 0
            amount_invested = 0
            for qs_c in qs_company:
                amount += qs_c.amount
                price_per_one += qs_c.price_per_one
                amount_invested += qs_c.amount_invested
            sum_dict['amount'] = amount
            sum_dict['price_per_one'] = round(price_per_one/len(qs_company),2)
            sum_dict['amount_invested'] = round(amount_invested, 2)
            context['shares'][qs.company_name]['sum'] = sum_dict
        return context

    # # Szkolenie eCommerce
    # def get_context_data(self, *args, **kwargs):
    #     context = super(PublicWalletsDetailView, self).get_context_data(*args, **kwargs)
    #     # context['abc'] = 123
    #     return context

class WalletCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account:login')

    template_name = 'stock_wallet/create_wallet.html'
    form_class = WalletModelForm
    success_url = reverse_lazy('stock_wallet:public_wallets')

    def get(self, request, *args, **kwargs):
        form = WalletModelForm()
        context = { 'form': form }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = WalletModelForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            form = WalletModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class PurchasedShareListView(ListView):
    model = PurchasedShare
    template_name = "stock_wallet/purchased_share_list.html"

    def get_queryset(self):
        object_list = get_object_or_404(Wallet, slug=self.kwargs.get('slug'))
        if object_list.is_private == True:
            if object_list.user == self.request.user:
                return object_list
            else:
                raise PermissionDenied
        else:
            return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(PurchasedShareListView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            purchased_shares = context['object_list'].purchasedshare_set.filter(company_name=self.kwargs.get('company_name'))
        else:
            raise PermissionDenied

        context['purchased_shares'] = purchased_shares
        return context

class PurchasedShareCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account:login')

    template_name = 'stock_wallet/purchased_share_create.html'
    form_class = WalletModelForm


    def get(self, request, *args, **kwargs):
        form = PurchasedShareModelForm()
        context = { 'form': form }
        return render(request, self.template_name, context)


# class WalletViewSet(viewsets.ModelViewSet):
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer
#
# class PurchasedShareViewSet(viewsets.ModelViewSet):
#     queryset = PurchasedShare.objects.all()
#     serializer_class = PurchasedShareSerializer
