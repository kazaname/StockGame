# Generated by Django 2.2.11 on 2020-03-18 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0008_auto_20200318_2104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Record',
            new_name='PurchasedShare',
        ),
    ]
