# Generated by Django 2.2.11 on 2020-03-18 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0006_auto_20200318_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='stock_records',
        ),
    ]
