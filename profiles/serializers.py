from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.IntegerField()
    following_count = serializers.SerializerMethodField()
    followers = serializers.ReadOnlyField()
    following = serializers.ReadOnlyField()

    name = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    
    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            # Implement your logic to get following_id
            return None  # Replace with your actual logic

    def get_following_count(self, obj):
        # Implement your logic to get following_count
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 
            'content', 'image', 'is_owner', 'following_id', 
            'posts_count', 'followers_count', 'following_count', 'following', 'followers',
        ]