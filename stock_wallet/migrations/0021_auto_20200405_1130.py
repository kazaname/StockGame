# Generated by Django 2.2.11 on 2020-04-05 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0020_remove_purchasedshare_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedshare',
            old_name='price_for_stocks',
            new_name='price_per_all',
        ),
        migrations.RenameField(
            model_name='purchasedshare',
            old_name='price_for_one_stock',
            new_name='price_per_one',
        ),
    ]
