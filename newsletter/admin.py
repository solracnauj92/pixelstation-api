from django.contrib import admin
from .models import SubscribedUsers

@admin.register(SubscribedUsers)
class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email') 
    search_fields = ('email', 'name')  
    ordering = ('name',)  

