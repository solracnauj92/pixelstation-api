from django.urls import path
from forums import views

urlpatterns = [
    path('forums/', views.ForumViewSet.as_view({'get': 'list'}), name='forum-list'),
    path('forums/<int:pk>/', views.ForumViewSet.as_view({'get': 'retrieve'}), name='forum-detail'),
    path('forums/<int:forum_id>/threads/', views.ThreadViewSet.as_view({'get': 'list'}), name='thread-list'),
    path('forums/<int:forum_id>/threads/<int:pk>/', views.ThreadViewSet.as_view({'get': 'retrieve'}), name='thread-detail'),
    path('forums/<int:forum_id>/threads/<int:thread_id>/posts/', views.PostViewSet.as_view({'get': 'list'}), name='forum-post-list'),
    path('forums/<int:forum_id>/threads/<int:thread_id>/posts/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve'}), name='forum-post-detail'),
]
