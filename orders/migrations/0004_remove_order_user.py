# Generated by Django 4.1.7 on 2023-03-09 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_billingaddress_order_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]