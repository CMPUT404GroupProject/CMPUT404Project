from http.client import HTTPResponse
from rest_framework import viewsets
from django.http import HttpResponse
from api.models import Post
from api.post.serializers.posts import PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
