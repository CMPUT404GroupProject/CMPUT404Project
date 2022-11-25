from rest_framework import serializers
from .models import Comment
from .models import Post, PostImage
from .models import Like
from .models import Inbox
from .models import FollowRequest
from .models import Follower
from api.user.serializers import UserSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['type', 'title', 'id', 'source', 'origin', 'description', 'contentType', 'content','author', 'categories', 'count', 'comments', 'published', 'visibility', 'unlisted']

class PostDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['type', 'title', 'id', 'source', 'origin', 'description', 'contentType', 'content', 'author', 'categories', 'count', 'comments', 'published', 'visibility', 'unlisted']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = UserSerializer(instance.author).data
        data['author']['id'] = data['author']['url']
        return data

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['post', 'image']
class FollowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowRequest
        fields = ['type', 'actor', 'object', 'summary']

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['followed', 'follower']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'type', 'author', 'post', 'comment', 'contentType', 'published']

class CommentDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'type', 'author', 'post', 'comment', 'contentType', 'published']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = UserSerializer(instance.author).data
        data['author']['id'] = data['author']['url']
        return data
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['context', 'summary', 'type', 'author', 'object', 'post', 'comment']

class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ['author', 'item', 'type']