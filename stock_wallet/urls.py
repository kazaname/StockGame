from django.urls import path, include, re_path
from .views import WalletsListView, WalletsDetailView, WalletCreateView, PurchasedShareListView
# from .views import WalletViewSet, PurchasedShareViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('wallets', WalletViewSet)
# router.register('purchased_shares', PurchasedShareViewSet)
app_name = 'stock_wallet'

urlpatterns = [
    path('', WalletsListView.as_view(), name='public_wallets'),
    path('create_wallet', WalletCreateView.as_view(), name='create_wallet'),
    path('<slug:slug>/', WalletsDetailView.as_view(), name='wallet_detail'),
    path('<slug:slug>/<str:company_name>/', PurchasedShareListView.as_view(), name='share_list'),

    # path('<int:id>/', PublicWalletsDetailView.as_view(), name='wallet_detail'), URL powiązany jest z detail view get_object
]
