from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(default=2000)
    platform = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='default_image_path.jpg')

    def __str__(self):
        return self.title


class GameCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.game.title}'