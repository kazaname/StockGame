# Generated by Django 2.2.11 on 2020-04-05 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0021_auto_20200405_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedshare',
            old_name='ammount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='purchasedshare',
            old_name='price_per_all',
            new_name='amount_invested',
        ),
    ]
