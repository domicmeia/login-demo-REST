import pytest

from rest_framework.exceptions import ValidationError

from login.apps.blog.api.v1.serializers.post import PostSerializer
from login.apps.accounts.models import UserAccount
from login.apps.blog.models import Post


@pytest.fixture()
def input_data():
    return {
        "title": "title",
        "text": "text",  # nosec
        "tags": "tag",
        "author": "author",
    }

@pytest.mark.django_db
def test_post_serializer_validate_success(input_data):
    serializer = PostSerializer(data=input_data)
    data = serializer.validate(input_data)
    assert data == input_data

@pytest.mark.django_db
def test_post_serializer_save_success(input_data):
    assert Post.objects.count() == 0

    serializer = PostSerializer(data=input_data)
    post = serializer.save()

    assert Post.objects.count() == 1
    assert Post.objects.get().pk == post.pk
    assert post.title == input_data["title"]
    assert post.text == input_data["text"]
    assert post.tags == input_data["tags"]
    assert post.author == input_data["author"]
