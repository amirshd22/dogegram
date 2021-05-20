from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255, null=True,blank=True)
    description = models.TextField(blank=True,null=True, max_length=2500)
    created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.user.username}-{self.title}'

class PostComment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=1200)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.content}"


class PostLike(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    value = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment,on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.value}"



