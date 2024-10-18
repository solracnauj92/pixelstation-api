from django.urls import path
from forums import views

urlpatterns = [
    path('forums/', views.ForumViewSet.as_view({'get': 'list'}), name='forum-list'),
    path('forums/<int:pk>/', views.ForumViewSet.as_view({'get': 'retrieve'}), name='forum-detail'),
    path('threads/', views.ThreadViewSet.as_view({'get': 'list'}), name='thread-list'),
    path('threads/<int:pk>/', views.ThreadViewSet.as_view({'get': 'retrieve'}), name='thread-detail'),
    path('posts/', views.PostViewSet.as_view({'get': 'list'}), name='post-list'),
    path('posts/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve'}), name='post-detail'),
]
