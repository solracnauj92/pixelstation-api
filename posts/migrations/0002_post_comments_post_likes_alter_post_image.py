# Generated by Django 5.0.6 on 2024-07-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('likes', '0002_alter_like_post'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='post_comments', to='comments.comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to='likes.like'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default_profile_path', upload_to='images/'),
        ),
    ]
