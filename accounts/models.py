from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"), unique=True)
    mobile_no = models.CharField(max_length=10, validators=[
                                 RegexValidator(r'^\d{10}$')])
    Address = models.TextField()
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    Pincode = models.CharField(max_length=6, validators=[
        RegexValidator(r'^\d{6}$')])
    is_superadmin = models.BooleanField(default=False)
    is_poolhost = models.BooleanField(default=False)
    is_pooluser = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    status = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email