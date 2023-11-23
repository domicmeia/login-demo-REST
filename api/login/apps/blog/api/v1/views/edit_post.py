from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from login.apps.blog.models import Post
from login.apps.blog.api.v1.serializers.post import PostSerializer

@extend_schema_view (
        get=extend_schema(
            summary="post",
            tags=["Blog"],
        ),
        put=extend_schema(
            summary="Update post",
            tags=["Blog"],
        ),
        patch=extend_schema(
            summary="Update post",
            tags=["Blog"],
        )
    )

class PostUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post = get_object_or_404(Post, uuid=self.kwargs['post_pk'], post_uuid=self.kwargs['post_pk'])
        self.check_object_permissions(self.request, post)
        return post

