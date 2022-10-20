from api.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'displayName','email', 'is_active', 'created', 'updated']
        read_only_field = ['displayName', 'is_active', 'created', 'updated']