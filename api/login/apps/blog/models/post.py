from django.db import models

from login.apps.accounts.models import UserAccount
from login.apps.common.models import CoreModel

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Post(CoreModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(UserAccount, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)

class Comment(CoreModel):
    author = models.ForeignKey(UserAccount, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
