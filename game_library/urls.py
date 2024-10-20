from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, GameCollectionViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet, basename='game')
router.register(r'collections', GameCollectionViewSet, basename='gamecollection')

urlpatterns = [
    path('', include(router.urls)),
]
