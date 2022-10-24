from http.client import HTTPResponse
from rest_framework import viewsets
from django.http import HttpResponse
from api.models import Post
from api.post.serializers.posts import PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        querySet = Post.objects.filter(author_id = self.kwargs.get('authorID')).filter(id=self.kwargs.get('postID'))
        return querySet