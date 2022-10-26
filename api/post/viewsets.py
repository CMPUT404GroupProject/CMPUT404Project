from http.client import HTTPResponse
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from api.models import Post, User
from api.post.serializers.posts import CreatePostSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put']
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
        if self.kwargs.get('postID'):
            querySet = Post.objects.filter(id = self.kwargs.get('id')).filter(id=self.kwargs.get('postID'))
        else:
            print(self.kwargs.get('id'))
            querySet = Post.objects.filter(author_id = self.kwargs.get('id'))
        return querySet
    
        
