from django.db import models
from siteadmin.models import Vehicle_Type
from accounts.models import User
from django.core.validators import RegexValidator
# from .managers import CustomUserManager

# Create your models here.


class vehicle_register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiclename = models.CharField(max_length=30)
    brandname = models.CharField(max_length=30)
    vehicle_image = models.ImageField(upload_to="vehicle_image", null=True, blank=True)
    number_plate = models.ImageField(upload_to="number_plate", null=True, blank=True)
    rc_image= models.ImageField(upload_to="rc_image", null=True, blank=True)
    Vehicle_Type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=20)
    capacity = models.CharField(max_length=2, validators=[
                                 RegexValidator(r'^\d{2}$')])
    fuel_capacity = models.CharField(max_length=2)
    status = models.CharField(max_length=10,default='pending')



    def __str__(self):
        return self.vehicle_name

# Create your models here.

# class VehicalRegister(models.Model):
#     Vehical_Name = models.CharField(max_length=30)
#     Vehical_Type = models.ForeignKey(VehicalType, on_delete=models.CASCADE)