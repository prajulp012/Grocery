# Generated by Django 4.2.1 on 2023-06-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_customer_forget_password_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered')], default='Order Placed', max_length=100),
        ),
    ]
