# Generated by Django 2.2.11 on 2020-03-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0009_auto_20200318_2111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SumRecords',
            new_name='SummaryPurchasedShare',
        ),
    ]