from rest_framework import serializers
from .models import Wallet, PurchasedShare

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'name', 'total_profit', 'created_at', 'updated_at']

class PurchasedShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedShare
        fields = ['id', 'user', 'wallet', 'company_name', 'short_name', 'ammount',
                  'price_for_one_stock', 'price_for_stocks', 'created_at', 'updated_at']