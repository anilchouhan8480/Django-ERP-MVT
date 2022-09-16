from django import forms
from .models import PoLine_Model


class PoLine_Form(forms.ModelForm):
     class Meta:
        model = PoLine_Model
        fields = ['PoLine_No','Description','Remark','Created_By',]

