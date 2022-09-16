from django import forms
from django.forms.widgets import TextInput
from .models import  Department_model

class Department_Forms(forms.ModelForm):
    class Meta:
        model = Department_model
        fields =['Department_Name','Created_By',
                'Description','Remark',]   