from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from api.user.serializers import UserSerializer
from api.user.models import User


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    github = serializers.URLField(required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['id', 'username', 'displayName', 'url','github', 'profileImage', 'password', 'is_active', 'created', 'updated']

    def create(self, validated_data):
        try:
            user = User.objects.get(github=validated_data['github'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user
