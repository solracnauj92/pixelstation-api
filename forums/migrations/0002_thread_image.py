# Generated by Django 3.2.23 on 2024-10-28 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='thread_images/'),
        ),
    ]