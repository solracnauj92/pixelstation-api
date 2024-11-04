from django.contrib import admin
from .models import NewsletterSubscription

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'created_at') 
    search_fields = ('email',)

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
