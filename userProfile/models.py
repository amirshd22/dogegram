from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.query_utils import select_related_descend

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    username = models.CharField(null=True, max_length=200)
    name = models.CharField(max_length=200,null=True)
    bio = models.TextField(null=True)
    followers = models.ManyToManyField(User, related_name="following", blank=True)
    followers_count = models.IntegerField(default=0,null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    profilePic = models.ImageField(blank=True, null=True,default="default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.username