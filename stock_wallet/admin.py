from django.contrib import admin
from .models import Wallet, PurchasedShare, Dividend


class DividendTabularInLine(admin.TabularInline):
    model = Dividend

class PurchasedShareAdmin(admin.ModelAdmin):
    inlines = [DividendTabularInLine]
    list_display = [ 'company_name', 'short_name', 'amount', 'price_per_one', 'amount_invested', 'created_at', 'updated_at']

class StockRecordTabularInLine(admin.TabularInline):
    model = PurchasedShare

class WalletAdmin(admin.ModelAdmin):
    inlines = [StockRecordTabularInLine]
    list_display = ['name', 'user', 'cash', 'total_profit', 'is_private', 'slug', 'created_at', 'updated_at']

class SummaryPurchasedShareAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'short_name', 'amount', 'price_per_one', 'amount_invested']


admin.site.register(Wallet, WalletAdmin)
admin.site.register(PurchasedShare, PurchasedShareAdmin)
