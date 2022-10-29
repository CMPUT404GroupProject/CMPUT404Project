from api.user.serializers import FollowersSerializer, UserSerializer
from api.user.models import User, Followers, FollowRequest
from rest_framework import viewsets
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.http import Http404
import uuid
from rest_framework.response import Response
from api.user.pagination import AuthorListPagination, FollowersListPagination


class UserViewSet(viewsets.ModelViewSet):
    pagination_class = AuthorListPagination
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
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
        summary = f"{actor.id} wants to follow {object.id}"
        
        if object.id == actor.id:
            raise ValidationError("Users cannot follow themselves")
        
        if Followers.objects.filter(followed=self.kwargs.get('id')).filter(follower=self.kwargs.get('foreign_author_id')):
            raise ValidationError(f"You already follow {object.displayName}")
            
        FollowRequest.objects.get_or_create(id=id, type=type, object=object, actor=actor, summary=summary)
        
        return Response(status=200)