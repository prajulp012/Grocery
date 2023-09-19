# Generated by Django 4.2.2 on 2023-06-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_checkoutaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered')], default='Order Placed', max_length=100),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered')], default='Order Placed', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(default='cart', max_length=100),
        ),
    ]