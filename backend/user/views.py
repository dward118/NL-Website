from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializer import (
    CustomTokenObtainPairSerializer,
    ExperienceSerializer,
    InstitutionSerializer,
    RegisterSerializer,
    )

class DefaultView(GenericAPIView):
    def get_object(self, id):
        return User.objects.get(id=id)

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#**needs to be authed**
#REMOVE id=1 THAT SETS THE DEFAULT VALUE AS 1
#WHICH IS BAD, THE VALUE NEEDS TO EITHER
#BE PASSED IN THROUGH THE FRONTEND
#OR SOMEHOW THE BACKEND FIGURES OUT AUTH
class InstitutionView(DefaultView):
    serializer_class = InstitutionSerializer

    def put(self, request, id=1):
        user = self.get_object(id)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ExperienceView(DefaultView):
    serializer_class = ExperienceSerializer

    def put(self, request, id=1):
        user = self.get_object(id)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
