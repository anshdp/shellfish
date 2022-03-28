# Generated by Django 3.2 on 2022-03-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft', '0012_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
