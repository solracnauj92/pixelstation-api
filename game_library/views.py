from rest_framework import generics, permissions
from .models import Game, UserGame
from .serializers import GameSerializer, UserGameSerializer
from profiles.models import Profile  

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view the list of games

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view game details

class UserGameList(generics.ListCreateAPIView):
    serializer_class = UserGameSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can add games

    def get_queryset(self):
        # Change to access UserGame based on the logged-in user
        return UserGame.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Create the UserGame with the currently logged-in user
        serializer.save(user=self.request.user)
