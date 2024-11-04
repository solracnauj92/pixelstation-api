# views.py

from rest_framework import generics
from .models import Forum, Thread, Reply
from .serializers import ForumSerializer, ThreadSerializer, ReplySerializer

class ForumList(generics.ListCreateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ForumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ThreadListCreate(generics.ListCreateAPIView):
    serializer_class = ThreadSerializer
    
    def get_queryset(self):
        return Thread.objects.filter(forum_id=self.kwargs['forum_id'])

class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class ReplyListCreate(generics.ListCreateAPIView):
    serializer_class = ReplySerializer
    
    def get_queryset(self):
        return Reply.objects.filter(thread_id=self.kwargs['thread_id'])
