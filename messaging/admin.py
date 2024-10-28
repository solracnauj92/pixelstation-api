from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'receiver', 'created_at')  
    search_fields = ('subject', 'content', 'sender__username', 'receiver__username')
    list_filter = ('sender', 'receiver', 'created_at')  
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)  