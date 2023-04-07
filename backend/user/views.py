from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .forms import UserCreationForm
from .models import User
from .serializer import UserSerializer

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'

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
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['GET'])
def get_data(request):
    user = User.objects.all()
    serializer = UserSerializer(user)
    return Response(serializer.data)
