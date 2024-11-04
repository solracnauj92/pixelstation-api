# newsletter/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import NewsletterSubscription
from .serializers import NewsletterSubscriptionSerializer
from pixelstation_api.permissions import IsOwnerOrReadOnly
from django.http import HttpResponseRedirect

def newsletter_root(request):
    return HttpResponseRedirect('/newsletter/subscriptions/')

class NewsletterSubscriptionView(generics.CreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        
        
        if NewsletterSubscription.objects.filter(email=email).exists():
            return Response({'msg': 'This email is already subscribed.'}, status=status.HTTP_400_BAD_REQUEST)

        
        return super().create(request, *args, **kwargs)

class NewsletterSubscriptionListView(generics.ListAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
    filter_backends = [DjangoFilterBackend]
