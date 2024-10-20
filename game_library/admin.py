from django.contrib import admin
from .models import Game, GameCollection


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'platform')
    search_fields = ('title', 'platform')
    list_filter = ('platform', 'release_year')
    ordering = ('-release_year',)

@admin.register(GameCollection)
class GameCollectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'added_at')
    search_fields = ('user__username', 'game__title')
    list_filter = ('added_at',)
    ordering = ('-added_at',)