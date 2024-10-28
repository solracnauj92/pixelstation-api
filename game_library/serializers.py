from rest_framework import serializers
from .models import Game, UserGame

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__' 

class UserGameSerializer(serializers.ModelSerializer):
    game_title = serializers.CharField(source='game.title', read_only=True)  
    added_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserGame
        fields = ['id', 'game', 'added_at', 'game_title']  