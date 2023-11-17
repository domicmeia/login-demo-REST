from django.urls import path

from login.apps.blog.api.v1.views import post

urlpatterns = [
    path('posts/', post.PostListCreateAPIView.as_view(), name='post_list'),
    path('posts/<uuid:pk>/', post.PostDetailsAPIView.as_view(), name='post_details'),
]
