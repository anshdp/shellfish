# Generated by Django 3.2 on 2022-02-21 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craft_seller', '0007_auto_20220214_1216'),
        ('craft', '0006_auto_20220221_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craft_seller.fishdetails', unique=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craft.user', unique=True),
        ),
    ]
