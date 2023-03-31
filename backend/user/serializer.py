from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    institution = serializers.CharField()
    experience = serializers.IntegerField()
    approved = serializers.BooleanField()
