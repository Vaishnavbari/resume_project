from django import forms 
from .models import *
class registration(forms.ModelForm):

    class Meta:
        model=contacts
        fields=["name","email","subject","yourmessage"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control s"}),
            "email": forms.EmailInput(attrs={"class":"form-control s"}),
            "subject": forms.TextInput(attrs={"class":"form-control s"}),
            "yourmessage":forms.TextInput(attrs={"class":"form-control s"}),
        }
    