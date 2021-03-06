# Generated by Django 3.2 on 2022-03-08 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craft_seller', '0007_auto_20220214_1216'),
        ('craft', '0011_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_status', models.CharField(max_length=50)),
                ('payment_type', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craft_seller.fishdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craft.user')),
            ],
        ),
    ]
