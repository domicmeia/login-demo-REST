from django.urls import path

from login.apps.blog.api.v1.views.post import (
    PostCreateAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
)

urlpatterns = [
    path('posts/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/list/', PostListAPIView.as_view(), name='post_list'),
    path('posts/update/<uuid:pk>/', PostUpdateAPIView.as_view(), name='post_update'),
    path('posts/delete/<uuid:pk>/', PostDestroyAPIView.as_view(), name='post_destroy')
]
