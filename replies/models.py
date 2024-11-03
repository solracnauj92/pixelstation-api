from django.db import models
from django.contrib.auth.models import User
from forums.models import ForumPost

class Reply(models.Model):
    """
    Reply model, related to User and ForumPost
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
