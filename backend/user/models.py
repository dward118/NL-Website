from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    institution = models.TextField( editable=True, null=False)
    experience = models.IntegerField(editable=True, null=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def is_approved(self):
        return self.approved
    
