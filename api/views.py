from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, PostImageSerializer, CommentSerializer, LikeSerializer, InboxSerializer, FollowRequestSerializer, FollowerSerializer, PostDetailedSerializer, CommentDetailedSerializer
from .models import Post, Comment, Like, Inbox, FollowRequest, Follower, PostImage
from api.user.models import User
from .pagination import FollowRequestPagination, LikedListPagination, LikesListPagination, InboxListPagination, PostListPagination, CommentListPagination, FollowerListPagination
from rest_framework.response import Response
from django.http import Http404
from .config import *
from api.user.serializers import UserSerializer

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
        url = request.build_absolute_uri() 
        url = url.split('/authors/')[1]
        request.data['comments'] = conf_host + 'authors/' + url[:-1] + "/" + newPostId + "/comments"
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
    serializer_class = PostDetailedSerializer
    pagination_class = PostListPagination

    def get_object(self):
        # get full url
        url = self.request.build_absolute_uri()
        url = url.split('/authors/')[1]
        try:
            post = Post.objects.get(id=self.kwargs.get('postID'))
            
            # Modify id field
            post.id = conf_host + 'authors/' + url[:-1]
            return post
        except Post.DoesNotExist:
            raise Http404
    
    def get_queryset(self):
        return super().get_queryset()
    
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
        url = request.build_absolute_uri()
        url = url.split('/authors/')[1]
        # Set comments to the request url plus the new post id
        request.data['comments'] =  conf_host + 'authors/' + url[:-1] + "/comments"
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
    
class PostImageView(viewsets.ModelViewSet):
    model = PostImage
    serializer_class = PostImageSerializer
    # Get all images for a post
    def get_queryset(self):
        return PostImage.objects.filter(post_id=self.kwargs.get('postID'))
    
    def getImg(self, request, *args, **kwargs):
        # Get images using postID
        postImage = PostImage.objects.filter(post_id = self.kwargs.get('postID'))
        serializer = PostImageSerializer(postImage, many=True)
        return Response(serializer.data)
    
    def createImg(self, request, *args, **kwargs):

        try:
            # Create new image from 'image' in request
            newImage = PostImage.objects.create(
                image = request.data['image'],
                post = Post.objects.get(id=self.kwargs.get('postID'))
            )
            # Save new image
            newImage.save()
            return Response(status=201)
        except:
            return Response(status=404)

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

        # Increment count of the post
        post.count += 1
        post.save()

        return super().create(request, *args, **kwargs)

class CommentDetailedView(viewsets.ModelViewSet):
    # Allow using post request to update
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = CommentDetailedSerializer

    def get_object(self):
        try:
            comment = Comment.objects.get(id=self.kwargs.get('commentID'))
            # Modify id field
            comment.id = self.request.build_absolute_uri()[:-1]
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
        # Increment count of the post
        post = Post.objects.get(id=self.kwargs.get('postID'))
        post.count += 1
        post.save()
        request.data['post'] = post.id
        return super().create(request, *args, **kwargs)
    

class LikePostView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    pagination_class = LikesListPagination
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
    pagination_class = LikesListPagination

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

class FollowRequestView(viewsets.ModelViewSet):
    serializer_class = FollowRequestSerializer
    pagination_class = FollowRequestPagination
    # Get only follow requests for this author
    def get_queryset(self):
        querySet = FollowRequest.objects.filter(object_id = self.kwargs.get('id'))
        return querySet
    
    # Override create
    def create(self, request, *args, **kwargs):
        # Get the displayname of the actor
        actor = User.objects.get(id=request.data.get('actor'))
        # Get the displayname of the object
        object = User.objects.get(id=self.kwargs.get('id'))
        # Check if request already exists with same actor and object
        if FollowRequest.objects.filter(actor_id=request.data.get('actor'), object_id=self.kwargs.get('id')).exists():
            return Response(status=400, data="Follow request already exists")
        # Check if actor and object are the same
        if request.data.get('actor') == self.kwargs.get('id'):
            return Response(status=400, data="Actor and object cannot be the same")
        # Check if actor is already following object
        if Follower.objects.filter(follower_id=request.data.get('actor'), followed_id=self.kwargs.get('id')).exists():
            return Response(status=400, data="Actor is already following object")
        request.data['summary'] = actor.displayName + " wants to follow " + object.displayName
        request.data['object'] = self.kwargs.get('id')
        # Create inbox item for object
        inbox = Inbox.objects.create(
            author = object,
            item = request.data
        )
        # Save
        return super().create(request, *args, **kwargs)

class FollowerView(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    pagination_class = FollowerListPagination
    
    # Get only followers for this author
    def get_queryset(self):
        querySet = Follower.objects.filter(followed_id = self.kwargs.get('id'))
        return querySet
    
class FollowerDetailedView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = FollowerSerializer

    # Get only followers for this author
    def get_object(self):
        try:
            querySet = Follower.objects.get(followed_id = self.kwargs.get('id'), follower_id = self.kwargs.get('foreign_author_id'))
            return querySet
        except Follower.DoesNotExist:
            raise Http404
    
    # Override put
    def put(self, request, *args, **kwargs):
        # Create a new follower
        
        # Get new follower id from url
        followerID = self.kwargs.get('foreign_author_id')
        # Get followed id from url
        followedID = self.kwargs.get('id')

        # Check that there is a follow request for this follower and followed
        if FollowRequest.objects.filter(actor_id=followerID, object_id=followedID).exists():
            # Create new follower
            follower = Follower.objects.create(
                follower_id = followerID,
                followed_id = followedID
            )
            # Save
            follower.save()
            return Response(status=200)
        else:
            return Response(status=400, data="No follow request exists for this follower and followed")
    