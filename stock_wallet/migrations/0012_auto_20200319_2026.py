# Generated by Django 2.2.11 on 2020-03-19 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_wallet', '0011_auto_20200318_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedshare',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SummaryPurchasedShare',
        ),
    ]
