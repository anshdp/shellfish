# Generated by Django 3.2 on 2022-02-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft_seller', '0006_alter_fishdetails_fishdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishdetails',
            name='fishCatogory',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fishdetails',
            name='fishColor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fishdetails',
            name='fishImage',
            field=models.CharField(max_length=100),
        ),
    ]
