from django.urls import path
from .views import ReplyViewSet

urlpatterns = [
    path('', ReplyViewSet.as_view({'get': 'list', 'post': 'create'}), name='reply-list'),
    path('<int:pk>/', ReplyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='reply-detail'),
]
