from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):
    """
    Serializer for the Reply model
    Adds extra fields when returning a list of Reply instances
    """
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Reply
        fields = [
            'id', 'author', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]

class ReplyDetailSerializer(ReplySerializer):
    """
    Serializer for the Reply model used in Detail view
    Post is a read-only field so that we don't have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
