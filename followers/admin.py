from django.contrib import admin
from .models import Follower

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'followed', 'created_at')
    list_filter = ('created_at', 'owner', 'followed')
    search_fields = ('owner__username', 'followed__username')
    ordering = ('-created_at',)

    def owner(self, obj):
        return obj.owner.username

    def followed(self, obj):
        return obj.followed.username

    owner.admin_order_field = 'owner__username'
    followed.admin_order_field = 'followed__username'
