# Generated by Django 4.2.1 on 2024-02-23 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_totals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='totals',
        ),
    ]
