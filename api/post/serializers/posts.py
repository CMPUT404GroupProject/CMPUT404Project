from urllib import request
from rest_framework import serializers
from api.models import Author, Post
import uuid

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['type', 'title', 'id', 'source', 'origin', 'description', 'contentType', 'author', 'categories', 'count', 'comments', 'published', 'visibility', 'unlisted']

class CreatePostSerializer(serializers.Serializer):

    def save(self, **kwargs):
        test = uuid.uuid4()

        author = Author.objects.get(id = self.context['authorID'])
        request = self.context['request']
        type = request.data["type"]
        title = request.data["title"]
        source = request.data["source"]
        origin = request.data["origin"]
        description = request.data["description"]
        contentType = request.data["contentType"]
        categories = request.data["categories"]
        count = request.data["count"]
        comments = request.data["comments"]
        visibility = request.data["visibility"]

        Post.objects.create(author = author, type = type, title = title,
        source = source, origin = origin, description = description, contentType = contentType,
        categories = categories, count = count, id = test, comments = comments, visibility = visibility)
