from django.http import JsonResponse
from rest_framework import generics, permissions
from .models import Game, UserGame
from .serializers import GameSerializer, UserGameSerializer
from profiles.models import Profile  

def index(request):
    """
    API index view that provides a welcome message and available endpoints.
    """
    return JsonResponse({
        'message': 'Welcome to the Game Library API!',
        'endpoints': {
            'games': '/game_library/games/',
            'user games': '/game_library/user-games/',
        }
    })

class GameList(generics.ListCreateAPIView):
    """
    API view to retrieve list of games or create a new game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view the list of games

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a specific game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view game details

class UserGameList(generics.ListCreateAPIView):
    """
    API view to list all UserGames or create a new UserGame for the authenticated user.
    """
    serializer_class = UserGameSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can add games

    def get_queryset(self):
        """
        Override to return the UserGame instances for the logged-in user.
        """
        return UserGame.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Override to set the user field when creating a UserGame.
        """
        serializer.save(user=self.request.user)
