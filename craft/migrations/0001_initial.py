# Generated by Django 3.2 on 2021-10-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('user_type', models.CharField(default='user', max_length=100)),
                ('status', models.CharField(default='diactive', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('phone_no', models.BigIntegerField()),
                ('created_date', models.DateField()),
            ],
        ),
    ]
