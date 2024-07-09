from django.contrib import admin
from .models import Follower

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user', 'followed_at')
    search_fields = ('user__username', 'followed_user__username')
    list_filter = ('followed_at',)
    ordering = ('-followed_at',)