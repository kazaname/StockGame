from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView
from .forms import ContactForm, WalletModelForm
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

    # # Szkolenie eCommerce
    # def get_context_data(self, *args, **kwargs):
    #     context = super(PublicWalletsDetailView, self).get_context_data(*args, **kwargs)
    #     # context['abc'] = 123
    #     return context

class WalletCreateView(CreateView):
    template_name = 'stock_wallet/create_wallet.html'
    form_class = WalletModelForm
    success_url = reverse_lazy('stock_wallet:public_wallets')

    def post(self, request, *args, **kwargs):
        form = WalletModelForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
        return super(WalletCreateView, self).form_valid(form)


# class WalletViewSet(viewsets.ModelViewSet):
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer
#
# class PurchasedShareViewSet(viewsets.ModelViewSet):
#     queryset = PurchasedShare.objects.all()
#     serializer_class = PurchasedShareSerializer
