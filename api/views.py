from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, InboxSerializer
from .models import Post, Comment, Like, Inbox
from api.user.models import User
from .pagination import LikedListPagination, InboxListPagination, PostListPagination, CommentListPagination
from rest_framework.response import Response
from django.http import Http404
from .config import *

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
    pagination_class = PostListPagination
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

        # Create an inbox item for all authors in the database
        for author in User.objects.all():
            # Create inbox item
            inbox = Inbox.objects.create(
                author = author,
                item = request.data
            )
            # Save inbox item
            inbox.save()

        return super().create(request, *args, **kwargs)

class PostDetailedView(viewsets.ModelViewSet):
    # Allow using post request to update
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = PostSerializer

    def get_object(self):
        # get full url
        url = self.request.build_absolute_uri()
        try:
            post = Post.objects.get(id=self.kwargs.get('postID'))
            # Modify id field
            post.id = url[:-1]

            return post
        except Post.DoesNotExist:
            raise Http404
    
    def get_serializer_context(self):
        return {'id': self.kwargs.get('id'), 'request': self.request}

    
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs.get('postID'))
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
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
    
    # Override delete requests
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    # Delete the post
    def destroy(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs.get('postID'))
        post.delete()
        return Response(status=204)
    
    # Override put requests
    def put(self, request, *args, **kwargs):
        newPostId = self.kwargs.get('postID')
        request.data['id'] = newPostId
        if request.data.get('author') is None:
            request.data['author'] = self.kwargs.get('id')
        # Set comments to the request url plus the new post id
        request.data['comments'] = request.build_absolute_uri() + "comments/"
        # Add new field type with default post
        request.data['type'] = "post"

        # Create an inbox item for all authors in the database
        for author in User.objects.all():
            # Create inbox item
            inbox = Inbox.objects.create(
                author = author,
                item = request.data
            )
            inbox.item['type'] = "post"
            # Save inbox item
            inbox.save()

        return super().create(request, *args, **kwargs)
    

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = CommentListPagination
    http_method_names = ['get', 'post', 'put', 'delete']

    # Get only comments for this post
    def get_queryset(self):
        querySet = Comment.objects.filter(post_id = self.kwargs.get('postID'))
        return querySet

    # Add post id before posting
    def create(self, request, *args, **kwargs):
        request.data['post'] = self.kwargs.get('postID')
        # Create inbox item for author of the post
        post = Post.objects.get(id=self.kwargs.get('postID'))
        # Create inbox item
        inbox = Inbox.objects.create(
            author = post.author,
            item = request.data
        )
        inbox.item['type'] = "comment"
        # Save inbox item
        inbox.save()
        return super().create(request, *args, **kwargs)

class CommentDetailedView(viewsets.ModelViewSet):
    # Allow using post request to update
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = CommentSerializer

    def get_object(self):
        try:
            comment = Comment.objects.get(id=self.kwargs.get('commentID'))
            # Modify id field
            comment.id = self.request.build_absolute_uri()
            return comment
        except Comment.DoesNotExist:
            raise Http404

    # Override delete requests
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    # Delete the comment
    def destroy(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=self.kwargs.get('commentID'))
        comment.delete()
        return Response(status=204)

    # Override put requests
    def put(self, request, *args, **kwargs):
        newCommentId = self.kwargs.get('commentID')
        request.data['id'] = newCommentId
        if request.data.get('author') is None:
            request.data['author'] = self.kwargs.get('id')
        # Add new field type with default post
        request.data['type'] = "comment"

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
        # Create inbox item for author of the post
        post = Post.objects.get(id=self.kwargs.get('postID'))
        # Create inbox item
        inbox = Inbox.objects.create(
            author = post.author,
            item = request.data
        )
        inbox.item['type'] = "like"
        # Save inbox item
        inbox.save()
        
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
        
        # Create inbox item for author of the comment
        comment = Comment.objects.get(id=self.kwargs.get('commentID'))
        # Create inbox item
        inbox = Inbox.objects.create(
            author = comment.author,
            item = request.data
        )
        inbox.item['type'] = "like"
        # Save inbox item
        inbox.save()

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


# View for author's inbox
class InboxView(viewsets.ModelViewSet):
    pagination_class = InboxListPagination
    serializer_class = InboxSerializer
    queryset = Inbox.objects.all()

    # Get only inbox items for this author
    def get_queryset(self):
        querySet = Inbox.objects.filter(author_id = self.kwargs.get('id'))
        return querySet

    # Add author id before posting
    def create(self, request, *args, **kwargs):
        request.data['author'] = self.kwargs.get('id')
        return super().create(request, *args, **kwargs)
    
    # Delete every inbox item for this author
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    # Delete every inbox item for this author
    def destroy(self, request, *args, **kwargs):
        inbox = Inbox.objects.filter(author_id = self.kwargs.get('id'))
        inbox.delete()
        return Response(status=204)
