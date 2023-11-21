import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.response import Response

from login.apps.blog.models import Post, Tag

@pytest.mark.django_db
class PostCreateAPIView:
    @classmethod
    def setup_class(cls):
        cls.url = reverse('api-v1-blog:post_create')

    def test_create_post(self):
        assert Post.objects.count() == 0
        data = {'title': 'title', 'text': 'text'}
        response = self.api_client.post(self.url, data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.count() == 1
        post = Post.objects.first()
        assert post.title == data['title']
        assert post.text == data['text']


@pytest.mark.django_db
class PostListAPIView:
    @classmethod
    def setup_class(cls):
        cls.url = reverse('api-v1-blog:post_list')

    def test_get_post_list(self):
        tag = Tag(name='tag_name')
        tag.save()
        post = Post(title='title1', text='text1')
        post.save()
        post.tags.add(tag)

        response = self.api_client.get(self.url)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert len(response_json) == 1
        data = response_json[0]
        assert data['title'] == post.title
        assert data['text'] == post.text
        assert data['tags'][0]['name'] == tag.name


@pytest.mark.django_db
class PostUpdateAPIView:
    @classmethod
    def setup_class(cls):
        cls.post = Post(title='title2', text='text2')
        cls.post.save()
        cls.url = reverse('api-v1-blog:post_update', kwargs={'pk': cls.post.pk})

    def test_update_post(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        data['title'] = 'new_title'
        data['text'] = 'new_text'
        response = self.client.put(self.url, data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.post.refresh_from_db()
        assert self.post.title == data['title']
        assert self.post.text == data['text']


@pytest.mark.django_db
class PostDestroyAPIView:
    @classmethod
    def setup_class(cls):
        cls.post = Post(title='title2', text='text2')
        cls.post.save()
        cls.url = reverse('api-v1-blog:post_destroy', kwargs={'pk': cls.post.pk})

    def test_delete_post(self):
        assert Post.objects.count() == 1
        response = self.client.delete(self.url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Post.objects.count() == 0
