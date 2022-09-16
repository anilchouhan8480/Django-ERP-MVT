from django import forms
from django.forms.widgets import TextInput
from .models import  UOM_model


class UOM_Forms(forms.ModelForm):
    class Meta:
        model =  UOM_model
        fields =['UOM','Created_By',
                'Description','Remark',]   