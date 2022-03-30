from django.db import models
from accounts.models import User
from django.core.validators import RegexValidator
# from .managers import CustomUserManager

class user_register(models.Model):
    User = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    emailid = models.EmailField()
    password = models.CharField(max_length=20)
