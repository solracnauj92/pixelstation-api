from rest_framework import serializers
from .models import Hub, Debate

class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = ['id', 'name', 'description', 'created_at']

class DebateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    hub_name = serializers.ReadOnlyField(source='hub.name')
    hub_description = serializers.ReadOnlyField(source='hub.description')

    class Meta:
        model = Debate
        fields = ['id', 'content', 'hub', 'hub_name', 'hub_description', 'author', 'created_at']
