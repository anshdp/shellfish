# Generated by Django 3.2 on 2022-03-09 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft', '0013_auto_20220309_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
