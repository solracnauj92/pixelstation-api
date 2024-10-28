from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')  

urlpatterns = [
    path('messages/<int:user_id>/', MessageViewSet.as_view({'get': 'list'})),  
    path('', include(router.urls)),
]
