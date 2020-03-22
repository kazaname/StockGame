# Generated by Django 2.2.11 on 2020-03-14 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0002_auto_20200314_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockwallet',
            name='stock_record',
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='stock_wallet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock_wallet.StockWallet'),
            preserve_default=False,
        ),
    ]