from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Like, FollowRequest, Inbox
from api.models import FollowRequest, Inbox, Follower
from api.user.models import User
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Inbox)
admin.site.register(Follower)
admin.site.register(FollowRequest)