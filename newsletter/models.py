from django.db import models

class NewsletterSubscription(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    email = models.EmailField(unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"