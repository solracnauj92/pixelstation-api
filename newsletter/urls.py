from django.urls import path
from .views import NewsletterSubscriptionListCreateView

urlpatterns = [
    path('subscriptions/', NewsletterSubscriptionListCreateView.as_view(), name='newsletter-subscriptions'),
]
