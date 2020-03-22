from django.contrib import admin
from .models import Wallet, PurchasedShare, Dividend


class DividendTabularInLine(admin.TabularInline):
    model = Dividend

class PurchasedShareAdmin(admin.ModelAdmin):
    inlines = [DividendTabularInLine]
    list_display = [ 'company', 'short_name', 'ammount', 'price_for_one_stock', 'price_for_stocks', 'created_at', 'updated_at']

class StockRecordTabularInLine(admin.TabularInline):
    model = PurchasedShare

class WalletAdmin(admin.ModelAdmin):
    inlines = [StockRecordTabularInLine]
    list_display = ['name', 'user', 'cash', 'total_profit', 'is_private', 'slug']

class SummaryPurchasedShareAdmin(admin.ModelAdmin):
    list_display = ['company', 'short_name', 'ammount', 'price_for_one_stock', 'price_for_stocks']


admin.site.register(Wallet, WalletAdmin)
admin.site.register(PurchasedShare, PurchasedShareAdmin)
