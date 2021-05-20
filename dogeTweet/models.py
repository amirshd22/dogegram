from django.db import models
from django.contrib.auth.models import User
import uuid


class Tweets(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    content = models.TextField(max_length=600, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class TweetComment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    content = models.TextField(max_length=600, null=True)
    tweet =  models.ForeignKey(Tweets,on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.content} {self.tweet}"


class UpVoteTweet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    value = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    comment = models.ForeignKey(TweetComment,on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.value}"

