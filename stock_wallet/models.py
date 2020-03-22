from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

class Wallet(models.Model):
    user                    = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=30, blank=False)
    total_profit            = models.DecimalField(max_digits=28, decimal_places=9, blank=True, null=True)
    cash                    = models.DecimalField(max_digits=28, decimal_places=4, blank=True, null=True)
    minimum_commission      = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True,
                                                  validators=[MinValueValidator(0),])
    percentage_commission   = models.FloatField(blank=True, null=True)
    is_private              = models.BooleanField(default=True)
    slug                    = models.SlugField(blank=True, null=True)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['-updated_at', 'total_profit']
        unique_together = [['user', 'name']]


class PurchasedShare(models.Model):
    wallet                  = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    company                 = models.CharField(max_length=120)
    short_name              = models.CharField(max_length=10)
    ammount                 = models.IntegerField(validators= [MinValueValidator(1),])
    price_for_one_stock     = models.DecimalField(max_digits=15, decimal_places=9)
    price_for_stocks        = models.DecimalField(max_digits=19, decimal_places=9, blank=True, null=True)
    share_price             = models.DecimalField(max_digits=12, decimal_places=4)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company

class Dividend(models.Model):
    stockrecord = models.ForeignKey(PurchasedShare, on_delete=models.CASCADE, blank=True, null=True)
    payment_date = models.DateField()
    ex_dividend_date = models.DateField()
    value_per_stock = models.DecimalField(max_digits=15, decimal_places=9)
    full_value = models.DecimalField(max_digits=15, decimal_places=9)
    yield_per_stock = models.DecimalField(max_digits=15, decimal_places=9)

def create_slug_name(sender, instance, *args, **kwargs):
    instance.name = instance.name.title()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def total_profit_calculator(sender, instance, *args, **kwargs):
    return

def stock_profit_calculator(sender, instance, *args, **kwargs):
    instance.price_for_stocks = instance.ammount * instance.price_for_one_stock
    print(instance.price_for_stocks)

pre_save.connect(create_slug_name, sender=Wallet)
pre_save.connect(stock_profit_calculator, sender=PurchasedShare)
