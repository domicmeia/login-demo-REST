import pytest

from rest_framework.exceptions import ValidationError

from login.apps.blog.api.v1.serializers.post import CommentSerializer
from login.apps.accounts.models import UserAccount
from login.apps.blog.models import Comment


@pytest.fixture()
def input_data():
    return {
        "author": "author",
        "post": "post"
    }

@pytest.mark.django_db
def test_comment_serializer_validate_success(input_data):
    serializer = CommentSerializer(data=input_data)
    data = serializer.validate(input_data)
    assert data == input_data

@pytest.mark.django_db
def test_comment_serializer_save_success(input_data):
    assert Comment.objects.count() == 0

    serializer = CommentSerializer(data=input_data)
    comment = serializer.save()

    assert Comment.objects.count() == 1
    assert Comment.objects.get().pk == comment.pk
    assert Comment.author == input_data["author"]
    assert Comment.post == input_data["post"]

