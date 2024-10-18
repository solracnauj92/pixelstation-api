from django.urls import path
from .views import GameViewSet, GameCollectionViewSet

urlpatterns = [
    path('game_library/games/', GameViewSet.as_view({'get': 'list'}), name='game-list'),
    path('game_library/games/<int:pk>/', GameViewSet.as_view({'get': 'retrieve'}), name='game-detail'),
    path('game_library/collections/', GameCollectionViewSet.as_view({'get': 'list'}), name='collection-list'),
    path('game_library/collections/<int:pk>/', GameCollectionViewSet.as_view({'get': 'retrieve'}), name='collection-detail'),
]
