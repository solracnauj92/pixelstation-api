from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, GameCollectionViewSet


router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'collections', GameCollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]