from django import forms
from django.forms.widgets import TextInput
from .models import TallyModel

class  Tally_Forms(forms.ModelForm):
     class Meta:
        model = TallyModel
        fields = ['Data_Name','Remark',
                       'Created_By','Transection_No',
        ]
