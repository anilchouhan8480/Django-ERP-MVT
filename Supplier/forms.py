from django import forms
from django.forms.widgets import Textarea, TextInput

from .models import Supplier_models


class Supplier_Forms(forms.ModelForm):
    class Meta:
        model = Supplier_models
        fields = ['Name', 'Email', 'Mobile_NO', 'GSTIN', 'Place_Of_Supply', 'suppliers_product',
                  'title', 'Billing_Name', 'Street_h_n', 'City', 'state', 'postalcode', 'country', 'Remark']
        labels = {
            'Mobile_NO': 'Mobile Number',
            'suppliers_product': 'Products',
            'Street_h_n': 'Street/House No.',
            'postalcode': 'Postal Code',

        }
        widgets = {
            'suppliers_product': Textarea(attrs={'placeholder': 'Enter Products', 'style': 'height:125px;border-color: #653D3E;border-width: 2px;border-radius: 6px;'}),
            'Remark': Textarea(attrs={'placeholder': 'Enter Remark ! Here', 'style': 'height:125px;border-color: #653D3E;border-width: 2px;border-radius: 6px;'}),
        }

    def __init__(self, *args, **kwargs):
        super(Supplier_Forms, self).__init__(*args, **kwargs)
        self.fields['state'].empty_label = 'Select State'
        self.fields['Place_Of_Supply'].empty_label = 'Select State'
