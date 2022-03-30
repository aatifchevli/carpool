from django.db import models

# Create your models here.

class admin_register(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    emailid = models.EmailField()
    password = models.CharField(max_length=10)

class Vehicle_Type(models.Model):
    vehicletype = models.CharField(max_length=20)
    vehiclename = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)