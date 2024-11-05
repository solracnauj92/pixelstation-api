from rest_framework import generics, permissions
from .models import Hub, Debate, Response
from .serializers import HubSerializer, DebateSerializer, ResponseSerializer

class HubList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hub.objects.all()
    serializer_class = HubSerializer

class DebateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user) 

class DebateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

class ResponseList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  

class ResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer