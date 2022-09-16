from django import forms
from django.forms.widgets import TextInput
from .models import  Branch_model


class Branch_Forms(forms.ModelForm):
    class Meta:
        model =  Branch_model
        fields =['Branch_Code','Branch_Name','Mobile_NO',
                 'Branch_add','City','state','Remark',]   
              
       