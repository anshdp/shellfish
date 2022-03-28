# Generated by Django 3.2 on 2022-02-21 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craft_seller', '0007_auto_20220214_1216'),
        ('craft', '0005_whishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craft_seller.fishdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craft.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Whishlist',
        ),
    ]
