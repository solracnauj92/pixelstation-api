from rest_framework import viewsets
from rest_framework import permissions 
from .models import Game, GameCollection
from .serializers import GameSerializer, GameCollectionSerializer

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to see the games


class GameCollectionViewSet(viewsets.ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = GameCollectionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can add to their collection

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user to the currently logged-in user
