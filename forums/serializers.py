from rest_framework import serializers
from .models import Forum, Thread, Reply, ForumPost

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost  # Ensure this model exists in your models.py
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
