from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.SerializerMethodField()
    followers = serializers.ReadOnlyField()
    following = serializers.ReadOnlyField()

    name = serializers.CharField(required=False, allow_blank=True) 
    content = serializers.CharField(required=False, allow_blank=True)  
    image = serializers.ImageField(required=False, allow_null=True)  

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:

            following = Follower.objects.filter(following=obj, follower=user).first()

            return following.id if following else None

        return None

    def get_following_count(self, obj):
        return obj.following.count()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 
            'content', 'image', 'is_owner', 'following_id', 
            'posts_count', 'followers_count', 'following_count', 'following', 'followers',
        ]
