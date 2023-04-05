from rest_framework import serializers
from djoser.conf import settings

from .models import User

class UserSerializer(serializers.ModelSerializer):
    #auth_token = serializers.CharField(source="key")
    is_staff = serializers.BooleanField(source="user.is_staff", read_only=True, default=False)

    class Meta:
        model=User
        fields='__all__'
