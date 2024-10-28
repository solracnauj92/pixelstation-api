from django.http import JsonResponse
from rest_framework import generics, permissions
from .models import Game, UserGame
from .serializers import GameSerializer, UserGameSerializer

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
    API view for the public game catalog.
    Allows anyone to view the list of games.
    Only authenticated users can add new games.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_permissions(self):
        # Public read access; authenticated users can create games
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific game.
    Allows anyone to view game details.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]

class UserGameList(generics.ListCreateAPIView):
    """
    API view for managing the user's game collection.
    Only authenticated users can access this.
    """
    serializer_class = UserGameSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can view or add to their collection

    def get_queryset(self):
        """
        Return the UserGame instances for the logged-in user.
        """
        return UserGame.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Set the user field when creating a UserGame in their collection.
        """
        serializer.save(user=self.request.user)
