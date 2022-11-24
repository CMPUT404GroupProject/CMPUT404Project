from xml.dom.expatbuilder import InternalSubsetExtractor
from api.user.serializers import FollowRequestSerializer, InboxSerializer, UserSerializer
from api.user.models import User
from api.models import FollowRequest, Inbox
from api.post.serializers.posts import PostSerializer
from rest_framework import viewsets
from django.core.exceptions import ValidationError
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.http import Http404
import uuid
from rest_framework.response import Response
from api.user.pagination import AuthorListPagination, InboxListPagination
from ..config import *

#@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    pagination_class = AuthorListPagination
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(id=lookup_field_value)
        self.check_object_permissions(self.request, obj)
        return obj
    
class UserDetailedViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    pagination_class = AuthorListPagination
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']
    def get_object(self):
        try:
            user = User.objects.get(id=self.kwargs.get('id'))
            # modify id field
            user.id = user.host + "authors/" + user.id
            return user
        except User.DoesNotExist:
            raise Http404
   
    def create(self, request, *args, **kwargs): 
        # Update the current user
        user = User.objects.get(id=self.kwargs.get('id'))
        data = request.data 
        # Add id to the data
        data['id'] = user.id
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400)
"""
class FollowersViewSet(viewsets.ModelViewSet):
    pagination_class = FollowersListPagination
    http_method_names = ['get', 'put', 'delete']
    serializer_class = UserSerializer
    
    def get_queryset(self):
        id = self.kwargs.get('id')
        followers = []
        for f in Followers.objects.filter(followed_id=id):
            follower = f.follower_id
            followers.append(follower)
            
        return User.objects.filter(id__in=followers)

class FollowersDetailedViewSet(viewsets.ModelViewSet):
    pagination_class = FollowersListPagination
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = UserSerializer
    
    def get_queryset(self):
        if self.request.method == 'DELETE':
            querySet = Followers.objects.filter(followed=self.kwargs.get('id')).filter(follower=self.kwargs.get('foreign_author_id'))
        elif self.request.method == 'PUT':
            querySet = Followers.objects.filter(followed=self.kwargs.get('id'))
        else:
            if Followers.objects.filter(followed=self.kwargs.get('id')).filter(follower=self.kwargs.get('foreign_author_id')):
                querySet = User.objects.filter(id=self.kwargs.get('foreign_author_id'))
            else:
                raise Http404
        return querySet
    
    def delete(self, *args, **kwargs):
        querySet = self.get_queryset().first()
        if not querySet:
            raise Http404
        querySet.delete()
        return Response(status=204)
    
    def put(self, request, *args, **kwargs):
        id = uuid.uuid4()
        type = "Follow"
        object = User.objects.get(id=kwargs['id'])
        actor = User.objects.get(id=kwargs['foreign_author_id'])
        summary = f"{actor.displayName} wants to follow {object.displayName}"
        
        if object.id == actor.id:
            raise ValidationError("Users cannot follow themselves")
        
        if Followers.objects.filter(followed=self.kwargs.get('id')).filter(follower=self.kwargs.get('foreign_author_id')):
            raise ValidationError(f"You already follow {object.displayName}")
        
        if FollowRequest.objects.filter(object=object).filter(actor=actor):
            raise ValidationError(f"You have already sent a follow request to this user")
        
        if not Inbox.objects.filter(author=object):
            Inbox.objects.create(author=object)
            
        follow_request = FollowRequest.objects.create(id=id, type=type, object=object, actor=actor, summary=summary, inbox=Inbox.objects.get(author=object))
                
        return Response(status=200)
"""

class InboxViewSet(viewsets.ModelViewSet):
    pagination_class = InboxListPagination
    
    # To see follow requests in inbox
    # serializer_class = FollowRequestSerializer
    
    # To see posts in inbox
    serializer_class = PostSerializer
    
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        # To see follow requests in inbox
        # querySet = Inbox.objects.get(author_id=self.kwargs.get('id')).followrequest_set.all()
        
        # To see posts in inbox
        querySet = Inbox.objects.get(author_id=self.kwargs.get('id')).post_set.all()
        
        return querySet