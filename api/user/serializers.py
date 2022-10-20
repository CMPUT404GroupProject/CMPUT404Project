from api.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['type', 'id', 'username', 'displayName', 'url', 'host','github', 'profileImage','is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']