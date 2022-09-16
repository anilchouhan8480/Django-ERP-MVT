from django import forms
from django.forms.widgets import TextInput
from .models import Color_Model

class  Color_Forms(forms.ModelForm):
     class Meta:
        model = Color_Model
        fields = ['Color_Name','Remark',
                       'Created_By',
        ]
