from django.urls import path
from forums import views

urlpatterns = [
    path('forums/', views.ForumViewSet.as_view({'get': 'list'}), name='forum-list'),
    path('forums/<int:forum_id>/', views.ForumViewSet.as_view({'get': 'retrieve'}), name='forum-detail'),
    path('forums/<int:forum_id>/threads/', views.ThreadViewSet.as_view({'get': 'list'}), name='thread-list'),
    path('forums/<int:forum_id>/threads/<int:thread_id>/', views.ThreadViewSet.as_view({'get': 'retrieve'}), name='thread-detail'),
    path('forums/<int:forum_id>/threads/<int:thread_id>/posts/', views.PostViewSet.as_view({'get': 'list'}), name='forum-post-list'),
    path('forums/<int:forum_id>/threads/<int:thread_id>/posts/<int:post_id>/', views.PostViewSet.as_view({'get': 'retrieve'}), name='forum-post-detail'),
]
