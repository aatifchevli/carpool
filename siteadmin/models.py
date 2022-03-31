from django.db import models
from accounts.models import User
# Create your models here.

class Vehicle_Type(models.Model):
    vehicletype = models.CharField(max_length=20)
    vehiclename = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)