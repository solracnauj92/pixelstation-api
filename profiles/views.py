from django.db.models import Count
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from .models import Profile
from .serializers import ProfileSerializer
from pixelstation_api.permissions import IsOwnerOrReadOnly

# Create your views here.
class ProfileList(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['post_count', 'followers_count', 'following_count', 'owner__following__created_at', 'owner__followed__created_at']

    def get_queryset(self, request):
        profiles = Profile.objects.annotate(
            post_count=Count('owner__post', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True)
        ).order_by('-created_at')

        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data) 

class ProfileDetail(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            profile = Profile.objects.annotate(
                post_count=Count('owner__post', distinct=True),
                followers_count=Count('owner__followed', distinct=True),
                following_count=Count('owner__following', distinct=True)
            ).get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

