from rest_framework import generics, permissions
from .models import Hub, Debate
from .serializers import HubSerializer, DebateSerializer

class HubList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hub.objects.all()
    serializer_class = HubSerializer

class HubDetail(generics.RetrieveAPIView):  # New view for hub detail
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hub.objects.all()
    serializer_class = HubSerializer

class HubDebateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DebateSerializer

    def get_queryset(self):
        hub_id = self.kwargs['hub_id']
        return Debate.objects.filter(hub_id=hub_id)

    def perform_create(self, serializer):
        hub = Hub.objects.get(id=self.kwargs['hub_id'])
        serializer.save(author=self.request.user, hub=hub)

class DebateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer