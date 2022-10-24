from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['type', 'title', 'id', 'source', 'origin', 'description', 'contentType', 'author', 'categories', 'count', 'comments', 'published', 'visibility', 'unlisted']

