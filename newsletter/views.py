# newsletter/views.py
from rest_framework import generics, permissions
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


class NewsletterSubscriptionListView(generics.ListAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
    filter_backends = [DjangoFilterBackend]
   
