# Generated by Django 2.2.11 on 2020-03-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockwallet',
            options={'ordering': ['-updated_at', 'total_profit']},
        ),
        migrations.AddField(
            model_name='stockwallet',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]