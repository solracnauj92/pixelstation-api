from django.db import models

class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True) 
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.email
