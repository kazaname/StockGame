# Generated by Django 2.2.11 on 2020-04-01 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0017_auto_20200401_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='total_profit',
            field=models.DecimalField(decimal_places=9, default=0, max_digits=28),
        ),
    ]
