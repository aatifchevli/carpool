from dataclasses import fields
from django import forms
from .models import *

class PoolUserForm(forms.ModelForm):
    class Meta:
        model = vehicle_register
        fields = ('username','firstname','lastname''emailid','password')
            