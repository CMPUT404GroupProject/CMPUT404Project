from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
# Import stuff for basic login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from api.user.serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        user = UserSerializer(self.user).data
        data['user'] = user
        data['token'] = Token.objects.get(user=self.user).key

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        # Remove refresh and access token from response
        data.pop('refresh')
        data.pop('access')
        return data


