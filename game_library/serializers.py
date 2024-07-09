from rest_framework import serializers
from .models import Game, GameCollection

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCollection
        fields = '__all__'