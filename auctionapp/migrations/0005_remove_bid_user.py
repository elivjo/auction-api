# Generated by Django 3.2.7 on 2021-09-29 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0004_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
    ]
