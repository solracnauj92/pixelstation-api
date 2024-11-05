from rest_framework import serializers
from .models import Hub, Debate, Response

class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = ['id', 'name', 'description', 'created_at']

class DebateSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')  

    class Meta:
        model = Debate
        fields = ['id', 'title', 'hub', 'creator', 'created_at']

class ResponseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  

    class Meta:
        model = Response
        fields = ['id', 'content', 'debate', 'author', 'created_at']