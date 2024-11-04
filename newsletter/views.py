from rest_framework import generics
from .models import NewsletterSubscription
from .serializers import NewsletterSubscriptionSerializer

class NewsletterSubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
