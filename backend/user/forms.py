from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

#used by django admin, not frontend
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "institution", "experience")

#used by django admin, not frontend
class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "institution", "experience", "approved")
