from urllib import request
from rest_framework import serializers
from api.models import Post
import uuid
from api.user.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['type', 'title', 'id', 'source', 'origin', 'description', 'contentType', 'author_key', 'categories', 'count', 'comments', 'published', 'visibility', 'unlisted']
