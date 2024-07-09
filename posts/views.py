from django.http import Http404
from rest_framework import status, permissions, filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer
from pixelstation_api.permissions import IsOwnerOrReadOnly


# class PostList(APIView):
#     serializer_class = PostSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]
#     filter_backends = [filters.OrderingFilter]
#     filterset_fields = [
#             'title',
#         ]
#     ordering_fields = ['created_at', 'comments_count', 'likes_count']

#     def get(self, request):
#         posts = Post.objects.annotate(
#             comments_count=Count('comments', distinct=True),
#             likes_count=Count('likes', distinct=True)
#         ).order_by('-created_at')
#         filter_backends = [
#             filters.OrderingFilter,
#             filters.SearchFilter,
#         ]
#         search_fields = [
#             'owner__username',
#             'title'
#         ]
#         filterset_fields = [
#             'title',
#         ]
#         serializer = PostSerializer(
#             posts, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all().order_by('-created_at')

    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    filter_backends = [filters.OrderingFilter]
    filterset_fields = [
            'title',
        ]
    ordering_fields = ['created_at', 'comments_count', 'likes_count']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(APIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            post = Post.objects.annotate(
                comments_count=Count('comments', distinct=True),
                likes_count=Count('likes', distinct=True)
            ).get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
