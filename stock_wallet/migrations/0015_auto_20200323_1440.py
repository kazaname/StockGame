# Generated by Django 2.2.11 on 2020-03-23 13:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_wallet', '0014_auto_20200322_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedshare',
            name='share_price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='minimum_commission',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterUniqueTogether(
            name='wallet',
            unique_together={('user', 'name')},
        ),
    ]