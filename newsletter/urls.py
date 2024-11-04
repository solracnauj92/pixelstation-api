from django.urls import path
from .views import NewsletterSubscriptionView, NewsletterSubscriptionListView, newsletter_root

urlpatterns = [
    path('', newsletter_root, name='newsletter_root'),  # Redirect or handle root
    path('subscriptions/', NewsletterSubscriptionView.as_view(), name='newsletter_subscribe'),
    path('subscriptions/list/', NewsletterSubscriptionListView.as_view(), name='newsletter_subscribe_list'),
]
