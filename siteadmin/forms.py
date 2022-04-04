from dataclasses import fields
from django import forms
from .models import*
from .models import User
from accounts.form import UserRegisterForm

class SiteAdmin(forms.ModelForm):
    class Meta:
        model = Registration_Form
        fields = ('firstname','lastname','emailid','password','address','gender',)             
