# Generated by Django 2.2.11 on 2020-03-18 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0010_auto_20200318_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedshare',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasedshare',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
