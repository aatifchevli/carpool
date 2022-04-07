from dataclasses import fields
from django import forms
from .models import *

class VehicleRegisterForm(forms.ModelForm):
    class Meta:
        model = vehicle_register
        fields = ('vehiclename',  'brandname', 'vehicle_image', 'number_plate',
                  'rc_image', 'Vehicle_Type', 'fuel_type', 'capacity', 'fuel_capacity')
        
class Vehicle_Type(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ('vehiclename','Vehicle_Type','brandname')