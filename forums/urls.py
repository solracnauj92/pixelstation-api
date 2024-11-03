from django.urls import path
from forums.views import ForumViewSet, ThreadViewSet, PostViewSet

urlpatterns = [
    path('', ForumViewSet.as_view({'get': 'list'}), name='forum-list'),
    path('<int:pk>/', ForumViewSet.as_view({'get': 'retrieve'}), name='forum-detail'),
    path('<int:forum_id>/threads/', ThreadViewSet.as_view({'get': 'list', 'post': 'create'}), name='thread-list'),
    path('<int:forum_id>/threads/<int:pk>/', ThreadViewSet.as_view({'get': 'retrieve'}), name='thread-detail'),
    path('<int:forum_id>/threads/<int:thread_id>/posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='forum-post-list'),
    path('<int:forum_id>/threads/<int:thread_id>/posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='forum-post-detail'),
]
