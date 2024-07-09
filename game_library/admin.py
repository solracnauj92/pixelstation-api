from django.contrib import admin
from .models import Game, GameCollection


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'release_date', 'platform')
    search_fields = ('title', 'developer', 'platform')
    list_filter = ('developer', 'platform', 'release_date')
    ordering = ('-release_date',)

@admin.register(GameCollection)
class GameCollectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'added_at')
    search_fields = ('user__username', 'game__title')
    list_filter = ('added_at',)
    ordering = ('-added_at',)