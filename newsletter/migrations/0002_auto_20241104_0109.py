# Generated by Django 3.2.23 on 2024-11-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedusers',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='subscribedusers',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
