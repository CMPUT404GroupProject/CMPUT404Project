from urllib import request
from urllib.error import HTTPError
from rest_framework import serializers
from api.models import Post, Inbox
import uuid
from api.user.models import User
from django.http import Http404

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['type', 'title', 'id', 'source', 'origin', 'description', 'contentType', 'author', 'categories', 'count', 'comments', 'published', 'visibility', 'unlisted']

class CreatePostSerializer(serializers.Serializer):

    def save(self, **kwargs):
        id = uuid.uuid4()

        author = User.objects.get(id = self.context['id'])
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

        post = Post.objects.create(author = author, type = type, title = title,
        source = source, origin = origin, description = description, contentType = contentType,
        categories = categories, count = count, id = id, comments = comments, visibility = visibility)
        
        for user in User.objects.all():
            if not Inbox.objects.filter(author=user):
                Inbox.objects.create(author=user)
            # Public posts
            if user != author:
                post.inbox.add(Inbox.objects.filter(author=user).first())

class UpdatePostSerializer(serializers.Serializer):


    def save(self, **kwargs):
        id = self.context['postID']
        if (Post.objects.filter(author_id = self.context['id']).filter(id=id).first()) == None:
            raise Http404

        post = Post.objects.get(author_id = self.context['id'], id = id)

        post.id = self.context['postID']
        post.author = User.objects.get(id = self.context['id'])
        request = self.context['request']
        post.type = request.data["type"]
        post.title = request.data["title"]
        post.source = request.data["source"]
        post.origin = request.data["origin"]
        post.description = request.data["description"]
        post.contentType = request.data["contentType"]
        post.categories = request.data["categories"]
        post.count = request.data["count"]
        post.comments = request.data["comments"]
        post.visibility = request.data["visibility"]

        post.save()



