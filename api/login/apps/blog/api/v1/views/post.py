from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from login.apps.blog.models import Post
from login.apps.blog.api.v1.serializers.post import PostSerializer

class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.active()

class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.active()