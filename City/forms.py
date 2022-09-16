from turtle import textinput
from typing import Text
from django import forms
from django.forms.widgets import TextInput
from .models import City_Model

class  City_Form(forms.ModelForm):
     class Meta:
        model =  City_Model
        fields = ['City_Name','Remark','Created_By',]

