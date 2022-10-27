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
            print("that post")
            return CreatePostSerializer
        return PostSerializer

    def get_serializer_context(self):
        return {'id': self.kwargs.get('id'),
        'request': self.request}
        
    def get_queryset(self):
        querySet = Post.objects.filter(author_id = self.kwargs.get('id'))
        return querySet

class UpdatePostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'post', 'delete', 'patch', 'head', 'options', 'trace']
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            print("this post")
            return UpdatePostSerializer
        return PostSerializer


    def get_serializer_context(self):
        return {'id': self.kwargs.get('id'),
        'postID': self.kwargs.get('postID'),
        'request': self.request}
        
    def get_queryset(self):
        querySet = Post.objects.filter(author_id = self.kwargs.get('id')).filter(id=self.kwargs.get('postID'))
        return querySet

    def delete(self, *args, **kwargs):
        querySet = self.get_queryset().first()
        if not querySet:
            raise Http404
        querySet.delete()
        return Response(status=204)
    