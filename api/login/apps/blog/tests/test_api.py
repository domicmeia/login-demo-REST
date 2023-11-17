import pytest

from rest_framework import status
from rest_framework.response import Response

from django.urls import reverse

from login.apps.blog.models import Post, Tag


@pytest.mark.django_db
def test_post_list_create_api(api_client):

    assert Post.objects.count() == 0
    data = {
        'title': 'title',
        'text': 'text'
    }
    response = api_client.post(reverse('api-v1-blog:post_list'), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.count() == 1
    post = Post.objects.first()
    assert post.title == data['title']
    assert post.text == data['text']

@pytest.mark.django_db
def test_get_post_list(api_client):
    tag = Tag(name='tag_name')
    tag.save()
    post = Post(title='title1', text='text1')
    post.save()
    post.tags.add(tag)

    response = api_client.get(reverse('api-v1-blog:post_list'))
    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) == 1
    data = response_json[0]
    assert data['title'] == post.title
    assert data['text'] == post.text
    assert data['tags'][0]['name'] == tag.name

@pytest.mark.django_db
def test_post_details_api(api_client):
    post = Post(title='title2', text='text2')
    post.save()
    response = api_client.get(reverse('api-v1-blog:post_details', kwargs={'pk': post.pk}))
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data['pk'] == str(post.pk)
    assert data['title'] == post.title
    assert data['text'] == post.text

@pytest.mark.django_db
def test_update_post(api_client):
    post = Post(title='title2', text='text2')
    post.save()
    response = api_client.get(reverse('api-v1-blog:post_details', kwargs={'pk': post.pk}))
    data = response.json()
    data['title'] = 'new_title'
    data['text'] = 'new_text'
    response = api_client.put(reverse('api-v1-blog:post_details', kwargs={'pk': post.pk}), data)
    assert response.status_code == status.HTTP_200_OK
    post.refresh_from_db()
    assert post.title == data['title']
    assert post.text == data['text']

@pytest.mark.django_db
def test_delete_post(api_client):
    post = Post(title='title2', text='text2')
    post.save()
    assert Post.objects.count() == 1
    response = api_client.delete(reverse('api-v1-blog:details', kwargs={'pk': post.pk}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Post.objects.count() == 0