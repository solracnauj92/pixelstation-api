
from rest_framework import serializers
from .models import Forum, Thread, Reply

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'title', 'created_at']

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'title', 'forum', 'created_at']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'content', 'thread', 'owner', 'created_at']
