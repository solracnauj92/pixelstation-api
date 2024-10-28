from rest_framework import serializers
from .models import Game, UserGame

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = ['id', 'game', 'added_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['game_title'] = instance.game.title
        return representation
