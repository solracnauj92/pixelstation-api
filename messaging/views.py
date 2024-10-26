from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        receiver_id = self.request.query_params.get('receiver', None)
        if receiver_id is not None:
            queryset = queryset.filter(receiver_id=receiver_id)
        return queryset
