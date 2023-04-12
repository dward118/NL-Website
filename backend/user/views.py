from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializer import UserSerializer, CustomTokenObtainPairSerializer

#@api_view(['POST']) #TODO COMBINE ALL INTO CLASSES
class SignUpView(GenericAPIView):
    serializer_class = UserSerializer

@api_view(['POST'])
def post_data(request):
    user = User.objects.all()
    serializer = UserSerializer(user)
    return Response(serializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['GET'])
def get_data(request):
    user = User.objects.all()
    serializer = UserSerializer(user)
    return Response(serializer.data)
