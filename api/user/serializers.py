from api.user.models import Followers, User
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
        fields = ['followed_user', 'follower']

class CreateFollowerSerializer(serializers.Serializer):
    
    def save(self, **kwargs):
        
        user_id = self.context['user_id']
        follower_id = self.context['follower_id']
        
        if user_id == follower_id:
            raise ValidationError("Users cannot follow themselves")
        
        Followers.objects.create(followed_user = user_id, follower = follower_id)
        
# class DeleteFollowerSerializer(serializers.Serializer):
    
#     def save(self, **kwargs):
        
#         user_id = self.context['user_id']
#         follower_id = self.context['follower_id']
        
#         try:
#             rel = Followers.objects.get(followed_user = user_id, follower = follower)
#             rel.delete()
#         except Followers.DoesNotExist:
#             return False
        
        
        