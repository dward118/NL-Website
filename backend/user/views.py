from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import UserCreationForm
from .models import User
from .serializer import UserSerializer

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@api_view(['GET'])
def get_data(request):
    user = User.objects.all()
    serializer = UserSerializer(user)
    return Response(serializer.data)
