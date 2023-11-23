from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from login.apps.blog.models import Comment
from login.apps.blog.api.v1.serializers.post import CommentSerializer

class CommentListCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.active()

    @extend_schema(
        summary="Comment Create", tags=["Blog"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()}
    )

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.active()

    @extend_schema(
        summary="Comment list", tags=["Blog"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()}
    )

    def get(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)