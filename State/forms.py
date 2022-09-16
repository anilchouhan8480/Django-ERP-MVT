from django import forms
from .models import State_Model
from django.forms.widgets import TextInput

class State_Form(forms.ModelForm):
     class Meta:
        model = State_Model
        fields = ['State_Name','Remark','Created_By',]


 
     '''widgets= {
            "Created_By":TextInput(attrs={'disabled':'True'}), 
        }'''
 