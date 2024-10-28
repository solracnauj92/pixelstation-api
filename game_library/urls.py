from django.urls import path
from .views import GameList, GameDetail, UserGameList

urlpatterns = [
    path('games/', GameList.as_view(), name='game-list'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game-detail'),
    path('user-games/', UserGameList.as_view(), name='user-game-list'),
]
