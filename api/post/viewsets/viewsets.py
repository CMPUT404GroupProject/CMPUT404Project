from http.client import HTTPResponse
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Post, User
from api.post.serializers.posts import CreatePostSerializer, PostSerializer, UpdatePostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.http import Http404


class CreatePostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'post', 'delete', 'patch', 'head', 'options', 'trace']
    # serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePostSerializer
        return PostSerializer

    def get_serializer_context(self):
        return {'id': self.kwargs.get('id'),
        'request': self.request}
        
    def get_queryset(self):
        querySet = Post.objects.filter(author_id = self.kwargs.get('id'))
        return querySet

class UpdatePostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'post', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UpdatePostSerializer
        return PostSerializer

    def get_serializer_context(self):
        return {'id': self.kwargs.get('id'),
        'postID': self.kwargs.get('postID'),
        'request': self.request}
        
    def get_queryset(self):
        if self.request.method != 'PUT':
            querySet = Post.objects.filter(author_id = self.kwargs.get('id')).filter(id=self.kwargs.get('postID'))
        else:
            querySet = Post.objects.filter(author_id = self.kwargs.get('id'))
        return querySet

    def delete(self, *args, **kwargs):
        querySet = self.get_queryset().first()
        if not querySet:
            raise Http404
        querySet.delete()
        return Response(status=204)
    
    def put(self, request, *args, **kwargs):
        

        id = kwargs['postID']
        author = User.objects.get(id = kwargs['id'])
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
        categories = categories, count = count, id = id, comments = comments, visibility = visibility)
        return Response(status=200)
    