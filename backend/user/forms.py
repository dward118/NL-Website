from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

# class UserCreationForm(UserCreationForm): #doesn't do anything currently
#     class Meta:
#         model = User
#         fields = ("username", "first_name", "last_name", "email", "institution", "experience")

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "institution", "experience", "approved")
