from django.urls import path, include, re_path
from .views import PublicWalletsListView, PublicWalletsDetailView
# from .views import WalletViewSet, PurchasedShareViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('wallets', WalletViewSet)
# router.register('purchased_shares', PurchasedShareViewSet)
app_name = 'stock_wallet'

urlpatterns = [
    path('', PublicWalletsListView.as_view(), name='public_wallets'),
    path('<slug:slug>/', PublicWalletsDetailView.as_view(), name='wallet_detail'),
]
