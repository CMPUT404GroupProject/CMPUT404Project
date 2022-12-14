from uuid import uuid4
from django.db import models
from datetime import datetime  
from api.user.models import User
import secrets
# Create your models here.

class Inbox(models.Model):
    type = "Inbox"
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'inbox_author')
    # Item is any single json object
    item = models.JSONField(null=True)

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
    type = models.CharField(max_length = 1024)
    title = models.CharField(max_length = 1024)
    id = models.CharField(max_length = 1024, primary_key=True)
    source = models.CharField(max_length = 1024)
    origin = models.CharField(max_length = 1024)
    description = models.TextField()
    contentType = models.CharField(max_length = 1024, default = "text/plain", blank = True, null = True)
    content = models.TextField(default = "", blank = True, null = True)
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'post_author')
    # Can use postgres if categories should be an arrayfield
    categories = models.CharField(max_length = 1024)
    # Count not required, default 0
    count = models.IntegerField(default = 0)
    comments = models.CharField(max_length = 1024, blank=True, null=True)
    #TODO not sure how comments and commentsSrc is supposed to work
    published = models.DateTimeField(default=datetime.now, blank=True, null=True)
    visibility = models.CharField(max_length = 1024, default = "PUBLIC", blank=True, null=True)
    unlisted = models.BooleanField(default = False)
    inbox = models.ManyToManyField(Inbox)   

class PostImage(models.Model):
    post = models.ForeignKey(Post, verbose_name= ("Post"), on_delete=models.CASCADE, related_name = 'post_image')
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)

class FollowRequest(models.Model):
    type = "Follow"
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actor")
    object = models.ForeignKey(User, on_delete=models.CASCADE, related_name="object", null=True, blank=True)
    summary = models.CharField(max_length=1024, default=f"You have a follow request")

class Comment(models.Model):
    type = models.CharField(max_length = 50, default="comment")
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'comment_author')
    post = models.ForeignKey(Post, verbose_name= ("Post"), on_delete=models.CASCADE, related_name = 'comment_post')
    comment = models.TextField()
    contentType = models.CharField(max_length = 1024)
    published = models.DateTimeField(default=datetime.now, blank=True)
    id = models.CharField(max_length = 1024, primary_key=True, default=generate_id)
    #post_id = models.CharField(max_length = 200, default="post_id")

class Like(models.Model):
    #TODO not sure what @context means
    context = models.CharField(max_length = 1024)
    summary = models.TextField()
    type = models.CharField(max_length = 1024)
    author = models.ForeignKey(User, verbose_name= ("Author"), on_delete=models.CASCADE, related_name = 'likes_author')
    object = models.CharField(max_length = 1024)
    post = models.ForeignKey(Post, verbose_name= ("Post"), on_delete=models.CASCADE, related_name = 'like_post', blank=True, null=True)
    comment = models.ForeignKey(Comment, verbose_name= ("Comment"), on_delete=models.CASCADE, related_name = 'like_comment', blank=True, null=True)

class Follower(models.Model):
    follower = models.ForeignKey(User, verbose_name= ("Follower"), on_delete=models.CASCADE, related_name = 'follower')
    followed = models.ForeignKey(User, verbose_name= ("Followed"), on_delete=models.CASCADE, related_name = 'followed')