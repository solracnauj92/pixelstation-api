from django.contrib import admin
from .models import Game, UserGame

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'genre') 
    search_fields = ('title',)

@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'added_at') 
    list_filter = ('user', 'game')
