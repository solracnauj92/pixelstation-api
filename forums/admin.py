from django.contrib import admin
from .models import Forum, Thread, ForumPost, Reply

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'creator', 'created_at')
    list_filter = ('forum', 'creator', 'created_at')
    search_fields = ('title', 'forum__name', 'creator__username')
    ordering = ('-created_at',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('content', 'thread', 'author', 'created_at')
    list_filter = ('thread__forum', 'author', 'created_at')
    search_fields = ('content', 'thread__title', 'author__username')
    ordering = ('-created_at',)

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'author', 'created_at')
    list_filter = ('post__thread__forum', 'author', 'created_at')
    search_fields = ('content', 'post__content', 'author__username')
    ordering = ('-created_at',)
