from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from api.user.models import User

import secrets
# Create your views here.
def generate_id():
    id = secrets.token_hex(32)
    """ #TODO - check if id already exists in database
    while True:
        id = secrets.token_hex(32)
        if User.objects.filter(id=code).count() == 0:
            break
    """
    return id

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get_serializer_context(self):
        return {'id': self.kwargs.get('id'),
        'request': self.request}
        
    def get_queryset(self):
        querySet = Post.objects.filter(author_id = self.kwargs.get('id'))
        return querySet

    # Add author id before posting if not specified
    def create(self, request, *args, **kwargs):
        newPostId = generate_id()
        if request.data.get('author') is None:
            request.data['author'] = self.kwargs.get('id')
        if request.data.get('id') is None:
            request.data['id'] = newPostId
        # Set comments to the request url plus the new post id
        request.data['comments'] = request.build_absolute_uri() + newPostId + "/comments/"
        # Add new field type with default post
        request.data['type'] = "post"

        return super().create(request, *args, **kwargs)

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # Get only comments for this post
    def get_queryset(self):
        querySet = Comment.objects.filter(post_id = self.kwargs.get('postID'))
        return querySet

    # Add post id before posting
    def create(self, request, *args, **kwargs):
        request.data['post'] = self.kwargs.get('postID')
        return super().create(request, *args, **kwargs)

class LikePostView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    # Get only likes for this post
    def get_queryset(self):
        querySet = Like.objects.filter(post_id = self.kwargs.get('postID'))
        return querySet

    # Add post id before posting
    def create(self, request, *args, **kwargs):
        request.data['post'] = self.kwargs.get('postID')
        likedObject = request.build_absolute_uri()
        # remove likes/ from the end of the url
        likedObject = likedObject[:-6]
        
        request.data['object'] = likedObject
        # Add new field with default context
        request.data['context'] = "http://www.w3.org/ns/activitystreams"
        # Add new field with default type
        request.data['type'] = "Like"
        # Get the displayname of the author
        author = User.objects.get(id=request.data.get('author'))
        request.data['summary'] = author.displayName + " Likes your post"
        return super().create(request, *args, **kwargs)

class LikeCommentView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    # Get only likes for this comment
    def get_queryset(self):
        querySet = Like.objects.filter(object_id = self.kwargs.get('commentID'))
        return querySet

    # Add comment id before posting
    def create(self, request, *args, **kwargs):
        request.data['object'] = self.kwargs.get('commentID')
        return super().create(request, *args, **kwargs)