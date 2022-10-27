from api.user.serializers import CreateFollowerSerializer, FollowersSerializer, UserSerializer
from api.user.models import User, Followers
from rest_framework import viewsets
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from api.user.pagination import AuthorListPagination, FollowersListPagination
from django.http import Http404

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
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = UserSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get('id')
        followers = []
        for f in Followers.objects.filter(followed_user=user_id):
            follower_id = f.follower
            followers.append(follower_id)
            
        return User.objects.filter(id__in=followers)

class FollowersDetailedViewSet(viewsets.ModelViewSet):
    pagination_class = FollowersListPagination
    http_method_names = ['get', 'post', 'put', 'delete']
    
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CreateFollowerSerializer
        else:
            return UserSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.kwargs.get('id'),
        'follower_id': self.kwargs.get('foreign_author_id')}
    
    def get_queryset(self):
        
        user_id = self.kwargs.get('id')
        follower_id = self.kwargs.get('foreign_author_id')
        
        return Followers.objects.filter(followed_user=user_id).filter(follower=follower_id)
    
    def delete(self, *args, **kwargs):
        querySet = self.get_queryset().first()
        if not querySet:
            raise Http404
        querySet.delete()
        return Response(status=204)