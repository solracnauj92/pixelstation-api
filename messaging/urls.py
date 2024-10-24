from django.urls import path
from .views import MessageViewSet

urlpatterns = [
    path('messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message-list'),
    path('messages/<int:pk>/', MessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='message-detail'),
]
