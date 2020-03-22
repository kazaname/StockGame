from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import ContactForm
from .models import Wallet, PurchasedShare
# from rest_framework import viewsets
# from .serializers import WalletSerializer, PurchasedShareSerializer

class PublicWalletsListView(ListView):
    queryset = Wallet.objects.filter(is_private=False)
    template_name = "stock_wallet/wallets_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PublicWalletsListView, self).get_context_data(*args, **kwargs)
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

class PublicWalletsDetailView(DetailView):
    model = Wallet
    # queryset = Wallet.objects.all()
    template_name = "stock_wallet/wallet_detail.html"


    # # Szkolenie eCommerce
    # def get_context_data(self, *args, **kwargs):
    #     context = super(PublicWalletsDetailView, self).get_context_data(*args, **kwargs)
    #     # context['abc'] = 123
    #     return context

# class WalletViewSet(viewsets.ModelViewSet):
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer
#
# class PurchasedShareViewSet(viewsets.ModelViewSet):
#     queryset = PurchasedShare.objects.all()
#     serializer_class = PurchasedShareSerializer
