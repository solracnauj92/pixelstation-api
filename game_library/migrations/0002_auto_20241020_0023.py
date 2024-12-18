# Generated by Django 3.2.23 on 2024-10-20 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game_library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='developer',
        ),
        migrations.RemoveField(
            model_name='game',
            name='release_date',
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(default='default_image_path.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='game',
            name='release_year',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gamecollection',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_library.game'),
        ),
        migrations.AlterField(
            model_name='gamecollection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
