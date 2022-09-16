from django import forms
from django.forms.widgets import TextInput
from .models import User_models

class User_forms(forms.ModelForm):
    class Meta:
        model =User_models
        fields =['User_Name',
                'Branch','Department',
                ]