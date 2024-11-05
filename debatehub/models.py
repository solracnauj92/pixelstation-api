from django.db import models
from django.contrib.auth.models import User

class Hub(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Debate(models.Model):  
    content = models.TextField(null=True, blank=True)
    hub = models.ForeignKey(Hub, related_name='debates', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='created_debates', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Debate by {self.author.username}"

class Response(models.Model):  
    content = models.TextField(null=True, blank=True)
    debate = models.ForeignKey(Debate, related_name='responses', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.author.username} in Debate by {self.debate.author.username}"
