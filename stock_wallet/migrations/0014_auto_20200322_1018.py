# Generated by Django 2.2.11 on 2020-03-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0013_wallet_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedshare',
            name='share_price',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wallet',
            name='minimum_commission',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='percentage_commission',
            field=models.FloatField(blank=True, null=True),
        ),
    ]