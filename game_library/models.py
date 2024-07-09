from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    release_date = models.DateField()
    platform = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class GameCollection(models.Model):
    user = models.ForeignKey(User, related_name='game_collections', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='collections', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.game.title}'