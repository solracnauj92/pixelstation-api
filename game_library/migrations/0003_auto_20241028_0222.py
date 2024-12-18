# Generated by Django 3.2.23 on 2024-10-28 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game_library', '0002_auto_20241020_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='game',
            old_name='platform',
            new_name='genre',
        ),
        migrations.RemoveField(
            model_name='game',
            name='release_year',
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default='No description available.'),
        ),
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='GameCollection',
        ),
        migrations.AddField(
            model_name='usergame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_games', to='game_library.game'),
        ),
        migrations.AddField(
            model_name='usergame',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_games', to=settings.AUTH_USER_MODEL),
        ),
    ]
