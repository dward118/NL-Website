from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    institution = models.TextField( editable=True, null=False)
    experience = models.IntegerField(editable=True, null=False)
    approved = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name", "email", "institution", "experience"]
