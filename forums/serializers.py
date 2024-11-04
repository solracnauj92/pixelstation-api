from rest_framework import serializers
from .models import Forum, Thread, Reply

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'name', 'description', 'created_at']  # Changed 'title' to 'name' and added 'description'

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'title', 'forum', 'creator', 'created_at']  # Ensure 'creator' is included as it's in the model

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'content', 'post', 'author', 'created_at']  # Changed 'owner' to 'author' and 'thread' to 'post' as per the model
