from rest_framework import serializers
from .models import Comment
from .models import Post
from .models import Like
from .models import Inbox

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['type', 'title', 'id', 'source', 'origin', 'description', 'contentType', 'author', 'categories', 'count', 'comments', 'published', 'visibility', 'unlisted']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'type', 'author', 'post', 'comment', 'contentType', 'published']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['context', 'summary', 'type', 'author', 'object', 'post', 'comment']

class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ['author']