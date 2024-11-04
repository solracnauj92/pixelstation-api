from django.urls import path
from .views import ForumList, ForumDetail, ThreadListCreate, ThreadDetail, ReplyListCreate

urlpatterns = [
    path('', ForumList.as_view(), name='forum-list'),  # List all forums
    path('<int:pk>/', ForumDetail.as_view(), name='forum-detail'),  # Retrieve, update, delete a specific forum
    path('<int:forum_id>/threads/', ThreadListCreate.as_view(), name='thread-list-create'),  # List or create threads for a specific forum
    path('threads/<int:pk>/', ThreadDetail.as_view(), name='thread-detail'),  # Retrieve, update, delete a specific thread
    path('threads/<int:thread_id>/replies/', ReplyListCreate.as_view(), name='reply-list-create'),  # List or create replies for a specific thread
]
