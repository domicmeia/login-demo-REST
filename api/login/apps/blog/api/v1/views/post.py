from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from login.apps.blog.models import Post, Comment
from login.apps.blog.api.v1.serializers.post import PostSerializer, CommentSerializer

class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer

    @extend_schema(
        summary="Post Create", tags=["Blog"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()}
    )

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer

    @extend_schema(
        summary="Post list", tags=["Blog"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()}
    )

    def get(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)