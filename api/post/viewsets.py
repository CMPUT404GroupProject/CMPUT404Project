from http.client import HTTPResponse
from api.user.serializers import UserSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from api.user.models import User

class PostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer

    def get_queryset(self):

        return User.objects.all()