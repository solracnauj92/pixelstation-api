# forums/models.py

from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Thread(models.Model):
    title = models.CharField(max_length=255)
    forum = models.ForeignKey(Forum, related_name='threads', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='created_threads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ForumPost(models.Model):
    content = models.TextField()
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='forum_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    content = models.TextField()
    post = models.ForeignKey(ForumPost, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
