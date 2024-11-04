from django.urls import path
from .views import ForumList, ForumDetail, ThreadListCreate, ThreadDetail, ReplyListCreate

urlpatterns = [
    path('', ForumList.as_view(), name='forum-list'),  # Change to '' for the list view
    path('<int:pk>/', ForumDetail.as_view(), name='forum-detail'),  # Keep the primary key
    path('<int:forum_id>/threads/', ThreadListCreate.as_view(), name='thread-list-create'),  # Adjust the thread path
    path('threads/<int:pk>/', ThreadDetail.as_view(), name='thread-detail'),
    path('threads/<int:thread_id>/replies/', ReplyListCreate.as_view(), name='reply-list-create'),
]
