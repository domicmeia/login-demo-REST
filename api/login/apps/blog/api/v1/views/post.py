from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
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
        super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # @extend_schema(
    #     get=extend_schema(
    #         summary="post",
    #         tags=["Blog"],
    #     ),
    #     put=extend_schema(
    #         summary="Udpate post",
    #         tags=["Blog"],
    #     ),
    #     patch=extend_schema(
    #         summary="Update post",
    #         tags=["Blog"],
    #     )
    # )

    def get_object(self):
        post = get_object_or_404(Post, uudi=self.kwargs['post_pk'], post_uuid=self.kwargs['post_pk'])
        self.check_object_permissions(self.request, post)
        return post

class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # @extend_schema(
    #     put=extend_schema(
    #         summary="Delete post",
    #         tags=["Blog"],
    #     ),
    #     patch=extend_schema(
    #         summary="Delete post",
    #         tags=["Blog"],
    #     )
    # )

    def get_object(self):
        post = get_object_or_404(Post, uudi=self.kwargs['post_pk'], post_uuid=self.kwargs['post_pk'])
        self.check_object_permissions(self.request, post)
        return post

class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.active()

class CommentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_object(self):
        comment = get_object_or_404(Comment, uudi=self.kwargs['comment_pk'], post_uuid=self.kwargs['post_pk'])
        self.check_object_permissions(self.request, comment)
        return comment