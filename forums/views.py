from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Forum, Thread, ForumPost  
from .serializers import ForumSerializer, ThreadSerializer, PostSerializer

class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        forum_id = self.kwargs.get('forum_id')
        if forum_id:
            return self.queryset.filter(forum_id=forum_id)
        return self.queryset

    def perform_create(self, serializer):
        forum_id = self.kwargs.get('forum_id')
        forum = Forum.objects.get(id=forum_id)
        serializer.save(creator=self.request.user, forum=forum)

class PostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()  
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)