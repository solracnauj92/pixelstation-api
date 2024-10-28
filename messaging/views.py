from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer  

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get_queryset(self):
        user = self.request.user  # Get the currently authenticated user
        # Return messages sent or received by the user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)
