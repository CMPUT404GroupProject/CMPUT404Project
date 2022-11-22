from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from api.user.models import User
from .pagination import LikedListPagination
from rest_framework.response import Response

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
    http_method_names = ['get', 'post', 'put', 'delete']
    
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

class PostDetailedView(viewsets.ModelViewSet):
    # Allow using post request to update
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get_serializer_context(self):
        return {'id': self.kwargs.get('id'),
        'request': self.request}
    
    def get_queryset(self):
        querySet = Post.objects.filter(id = self.kwargs.get('postID'))
        return querySet
    
    def create(self, request, *args, **kwargs):         
        # Update the current post
        post = Post.objects.get(id=self.kwargs.get('postID'))
        data = request.data 
        # Add id to the data
        data['id'] = post.id
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400)
    

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
        querySet = Like.objects.filter(comment_id = self.kwargs.get('commentID'))
        return querySet

    # Add comment id before posting
    def create(self, request, *args, **kwargs):
        request.data['comment'] = self.kwargs.get('commentID')
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
        request.data['summary'] = author.displayName + " Likes your comment"
        return super().create(request, *args, **kwargs)

# View to show liked posts and comments for a author
class LikedView(viewsets.ModelViewSet):
    pagination_class = LikedListPagination
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    # Get only likes for this author
    def get_queryset(self):
        querySet = Like.objects.filter(author_id = self.kwargs.get('id'))
        return querySet
    