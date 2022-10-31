from asyncore import read
from api.user.models import Followers, User
from api.models import FollowRequest, Inbox, Post
import uuid
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['type', 'id', 'url', 'host', 'displayName', 'github', 'profileImage']
        read_only_field = ['is_active', 'created', 'updated']

class FollowersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Followers
        fields = ['type', 'followed', 'follower']
        read_only_field = ['created', 'id']
        
class FollowRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FollowRequest
        fields = ['type', 'actor', 'object', 'summary']
        read_only_field = ['created', 'inbox', 'id']
        
        
class InboxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inbox
        fields = ['author']