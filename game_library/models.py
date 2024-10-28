from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile  

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")
    genre = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)  
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_games')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s collection of {self.game.title}"
