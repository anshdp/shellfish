# Generated by Django 3.2 on 2022-03-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft', '0015_rename_quantity_cart_p_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
