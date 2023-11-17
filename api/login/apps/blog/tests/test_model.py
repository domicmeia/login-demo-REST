import pytest

from login.apps.blog.models import Tag, Post

@pytest.mark.django_db
def test_post():
    assert Post.objects.count() == 0
    Post.objects.create(title='active', text='text', is_active=True)
    Post.objects.create(title='inactive', text='text', is_active=False)

    assert Post.objects.count() == 2

    active_posts = Post.objects.active()
    assert active_posts.count() == 1

    inactive_posts = Post.objects.inactive()
    assert inactive_posts.count() == 1

@pytest.mark.django_db
def test_tag():
    assert Tag.objects.count() == 0

    Tag.objects.create(name='name')
    assert Tag.objects.count() == 1