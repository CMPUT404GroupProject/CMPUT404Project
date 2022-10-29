from api.user.models import FollowRequest, Followers, User
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
        fields = ['id', 'type', 'followed', 'follower', 'created']
        read_only_field = ['created']
        
class FollowRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FollowRequest
        fields = ['id', 'type', 'actor', 'object', 'summary']
        read_only_field = ['created']
        