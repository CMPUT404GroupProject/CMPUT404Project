from uuid import uuid4
from django.db import models
from datetime import datetime  
from api.user.models import User
import secrets
# Create your models here.

class Inbox(models.Model):
    author = models.OneToOneField(User, default="author", on_delete=models.CASCADE, primary_key=True) 

def generate_id():
    id = secrets.token_hex(32)
    """ #TODO - check if id already exists in database
    while True:
        id = secrets.token_hex(32)
        if User.objects.filter(id=code).count() == 0:
            break
    """
    return id

class Post(models.Model):
    type = models.CharField(max_length = 50)
    title = models.CharField(max_length = 200)
    id = models.CharField(max_length = 200, primary_key=True)
    source = models.CharField(max_length = 200)
    origin = models.CharField(max_length = 200)
    description = models.TextField()
    contentType = models.CharField(max_length = 50)
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'post_author')
    # Can use postgres if categories should be an arrayfield
    categories = models.CharField(max_length = 50)
    count = models.IntegerField()
    comments = models.CharField(max_length = 200)
    #TODO not sure how comments and commentsSrc is supposed to work
    published = models.DateTimeField(default=datetime.now, blank=True)
    visibility = models.CharField(max_length = 50)
    unlisted = models.BooleanField(default = False)
    inbox = models.ManyToManyField(Inbox)   

class FollowRequest(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    type = models.CharField(max_length=50, default="Follow")
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actor")
    object = models.ForeignKey(User, on_delete=models.CASCADE, related_name="object")
    summary = models.CharField(max_length=500, default=f"You have a follow request")
    created = models.DateTimeField(default=datetime.now, blank=True)
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)

class Comment(models.Model):
    type = models.CharField(max_length = 50, default="comment")
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'comment_author')
    comment = models.TextField()
    contentType = models.CharField(max_length = 50)
    published = models.DateTimeField(default=datetime.now, blank=True)
    id = models.CharField(max_length = 200, primary_key=True, default=generate_id)
    #post_id = models.CharField(max_length = 200, default="post_id")

class Like(models.Model):
    #TODO not sure what @context means
    context = models.CharField(max_length = 50)
    summary = models.TextField()
    type = models.CharField(max_length = 50)
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'likes_author')
    object = models.CharField(max_length = 200)