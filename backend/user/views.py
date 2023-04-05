from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from djoser.views import TokenCreateView

from .models import User
from .serializer import UserSerializer

class TokenCreateView(TokenCreateView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        super().serializer_class = UserSerializer

    def _action(self, attrs):
        print("validate 20")
        ## This data variable will contain refresh and access tokens
        data = super()._action(attrs)
        print(User.institution) # <---
        data['institution'] = User.institution # <---
        ## You can add more User model's attributes like username,email etc. in the data dictionary like this.

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
