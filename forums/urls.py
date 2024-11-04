from django.urls import path
from .views import ForumList, ForumDetail, ThreadListCreate, ThreadDetail, ReplyListCreate

urlpatterns = [
    path("forums/", ForumList.as_view(), name="forum-list"),
    path("forums/<int:pk>/", ForumDetail.as_view(), name="forum-detail"),
    path("forums/<int:forum_id>/threads/", ThreadListCreate.as_view(), name="thread-list-create"),
    path("threads/<int:pk>/", ThreadDetail.as_view(), name="thread-detail"),
    path("threads/<int:thread_id>/replies/", ReplyListCreate.as_view(), name="reply-list-create"),
]
