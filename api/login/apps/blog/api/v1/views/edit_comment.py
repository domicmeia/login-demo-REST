from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from login.apps.blog.models import Comment
from login.apps.blog.api.v1.serializers.post import CommentSerializer

@extend_schema_view (
        get=extend_schema(
            summary="comment",
            tags=["Blog"],
        ),
        put=extend_schema(
            summary="Update comment",
            tags=["Blog"],
        ),
        patch=extend_schema(
            summary="Update comment",
            tags=["Blog"],
        )
    )

class CommentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_object(self):
        comment = get_object_or_404(Comment, uuid=self.kwargs['comment_pk'], post_uuid=self.kwargs['post_pk'])
        self.check_object_permissions(self.request, comment)
        return comment