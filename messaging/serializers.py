from rest_framework import serializers
from .models import Message
from .models import Profile


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'subject', 'content', 'created_at'] 
