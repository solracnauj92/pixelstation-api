from django.urls import path
from .views import GameViewSet, GameCollectionViewSet

urlpatterns = [
    path('games/', GameViewSet.as_view({'get': 'list'}), name='game-list'),
    path('games/<int:pk>/', GameViewSet.as_view({'get': 'retrieve'}), name='game-detail'),
    path('collections/', GameCollectionViewSet.as_view({'get': 'list'}), name='collection-list'),
    path('collections/<int:pk>/', GameCollectionViewSet.as_view({'get': 'retrieve'}), name='collection-detail'),
]
