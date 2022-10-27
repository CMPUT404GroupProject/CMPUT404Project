from django.db import models
from datetime import datetime  
from api.user.models import User

# Create your models here.


class Request(models.Model):
    # Friend or Follow
    type = models.CharField(max_length = 50)
    summary = models.TextField()
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'request_author')
    object = models.ForeignKey(User, verbose_name= ("Object"), on_delete=models.CASCADE, related_name = 'request_object')

class Comment(models.Model):
    type = models.CharField(max_length = 50)
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'comment_author')
    comment = models.TextField()
    contentType = models.CharField(max_length = 50)
    published = models.DateTimeField(default=datetime.now, blank=True)
    id = models.CharField(max_length = 200, primary_key=True)

class Post(models.Model):
    type = models.CharField(max_length = 50)
    title = models.CharField(max_length = 200)
    id = models.CharField(max_length = 200, primary_key=True)
    source = models.CharField(max_length = 200)
    origin = models.CharField(max_length = 200)
    description = models.TextField()
    contentType = models.CharField(max_length = 50)
    author_key = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'post_author')
    # Can use postgres if categories should be an arrayfield
    categories = models.CharField(max_length = 50)
    count = models.IntegerField()
    comments = models.CharField(max_length = 200)
    #TODO not sure how comments and commentsSrc is supposed to work
    published = models.DateTimeField(default=datetime.now, blank=True)
    visibility = models.CharField(max_length = 50)
    unlisted = models.BooleanField(default = False)

class Like(models.Model):
    #TODO not sure what @context means
    context = models.CharField(max_length = 50)
    summary = models.TextField()
    type = models.CharField(max_length = 50)
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'likes_author')
    object = models.CharField(max_length = 200)