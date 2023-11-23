# import pytest

# from django.urls import reverse

# from rest_framework import status

# from login.apps.blog.models import Post

# @pytest.mark.django_db
# def test_create_post(unauthorized_api_client):
#     assert Post.objects.count() == 0
#     data = {'title': 'title', 'text': 'text', 'author': 'author'}
#     response = unauthorized_api_client.post(reverse('api-v1-blog:post_create'), data)

#     assert response.status_code == status.HTTP_201_CREATED
#     assert Post.objects.count() == 1
#     post = Post.objects.first()
#     assert post.title == data['title']
#     assert post.text == data['text']

# @pytest.mark.django_db
# def test_get_post_list(unauthorized_api_client):
#     url = reverse('api-v1-blog:post_list')
#     tag = Tag(name='tag_name')
#     tag.save()
#     post = Post(title='title1', text='text1')
#     post.save()
#     post.tags.add(tag)
#     response = unauthorized_api_client.get(url)
#     response_json = response.json()
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response_json) == 1
#     data = response_json[0]
#     assert data['title'] == post.title
#     assert data['text'] == post.text
#     assert data['tags'][0]['name'] == tag.name


# @pytest.mark.django_db
# def test_update_post(unauthorized_api_client):
#     post = Post(title='title2', text='text2')
#     post.save()
#     url = reverse('api-v1-blog:post_update', kwargs={'pk': post.pk})
#     response = unauthorized_api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK
#     data = response.json()
#     data['title'] = 'new_title'
#     data['text'] = 'new_text'
#     response = unauthorized_api_client.put(url, data=data, format='json')
#     assert response.status_code == status.HTTP_200_OK
#     unauthorized_api_client.post.refresh_from_db()
#     assert unauthorized_api_client.post.title == data['title']
#     assert unauthorized_api_client.post.text == data['text']


# @pytest.mark.django_db
# def test_delete_post(unauthorized_api_client):
#     post = Post(title='title2', text='text2')
#     post.save()
#     url = reverse('api-v1-blog:post_destroy', kwargs={'pk': post.pk})
#     assert Post.objects.count() == 1
#     response = unauthorized_api_client.delete(url)
#     assert response.status_code == status.HTTP_204_NO_CONTENT
#     assert Post.objects.count() == 0
