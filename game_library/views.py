from rest_framework import viewsets
from .models import Game, GameCollection
from .serializers import GameSerializer, GameCollectionSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameCollectionViewSet(viewsets.ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = GameCollectionSerializer

