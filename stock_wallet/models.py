from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class StockWallet(models.Model):
    name = models.CharField(max_length=30, blank=False)
    total_profit = models.DecimalField(max_digits=28, decimal_places=9)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    stock_record = models.ForeignKey('StockRecord', on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StockRecord(models.Model):
    company = models.CharField(max_length=120)
    short_name = models.CharField(max_length=10)
    ammount = models.IntegerField(validators= [MinValueValidator(1),])
    price_for_one_stock = models.DecimalField(max_digits=15, decimal_places=9)
    price_for_stocks = models.DecimalField(max_digits=19, decimal_places=9)
    divident = models.ForeignKey('Dividend', on_delete=models.CASCADE)

class Dividend(models.Model):
    payment_date = models.DateField()
    ex_dividend_date = models.DateField()
    value_per_stock = models.DecimalField(max_digits=15, decimal_places=9)
    full_value = models.DecimalField(max_digits=15, decimal_places=9)
    yield_per_stock = models.DecimalField(max_digits=15, decimal_places=9)