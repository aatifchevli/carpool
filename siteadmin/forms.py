from dataclasses import fields
from django import forms
from .models import*

class SiteAdmin(forms.ModelForm):
    class Meta:
        modle = Registration_Form
        fields = ('firstname','lastname','emalid','password','address','gender',) 
