from django.urls import path
from .views import NewsletterSubscriptionView, subscribe

urlpatterns = [
    path('subscriptions/', NewsletterSubscriptionView.as_view(), name='newsletter_subscribe'),
]