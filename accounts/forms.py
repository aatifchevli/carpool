from dataclasses import fields
from django import forms
from .models import *

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',  'password', 'first_name', 'last_name',
                  'mobile_no', 'Address', 'City', 'State', 'Pincode', 'profile_pic')
        widgets = {
            'password': forms.PasswordInput()
        }
