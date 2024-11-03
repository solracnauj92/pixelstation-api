from rest_framework import generics, permissions
from pixelstation_api.permissions import IsOwnerOrReadOnly
from .models import Reply
from .serializers import ReplySerializer, ReplyDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ReplyList(generics.ListCreateAPIView):
    """
    List all replies
    Create a new reply if authenticated
    Associate the current logged in user with the reply
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a reply
    Update or delete a reply if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReplyDetailSerializer
    queryset = Reply.objects.all()
