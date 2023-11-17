from rest_framework import serializers

from login.apps.accounts.models import UserAccount
from login.apps.blog.models import Tag, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = {'pk', 'email', 'first_name', 'last_name', }

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = {'pk', 'name', }

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = {'pk', 'title', 'text', 'tags', 'author', }