from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "institution", "experience", "approved"]

class RegisterSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["username", "first_name", "last_name", "email", "institution", "experience"]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['institution'] = user.institution
        token['experience'] = user.experience
        token['approved'] = user.approved

        return token
