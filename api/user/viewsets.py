from api.user.serializers import UserSerializer
from api.user.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from api.user.pageAuthorList import AuthorListPagination


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