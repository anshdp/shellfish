# Generated by Django 3.2 on 2022-02-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft_seller', '0005_fishdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishdetails',
            name='fishDescription',
            field=models.TextField(),
        ),
    ]
