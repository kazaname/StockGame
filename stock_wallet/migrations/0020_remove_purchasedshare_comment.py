# Generated by Django 2.2.11 on 2020-04-05 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0019_auto_20200404_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedshare',
            name='comment',
        ),
    ]
