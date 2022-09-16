from django import forms
from .models import Payment_vouchers
from django.forms.widgets import TextInput

class Voucher_forms(forms.ModelForm):
     class Meta:
        model = Payment_vouchers
        fields =['Supplier_Name','Tally_data','Payment_amount','Bill_No','payment_date','payment_type','Transection_No','description']
        widgets = {
            'payment_date':TextInput(attrs={'type':'date'})

            }

      
     def __init__(self,*args,**kwargs):
            super(Voucher_forms,self).__init__(*args,**kwargs)
            self.fields['Supplier_Name'].empty_label='Select Supplier'
            self.fields['Tally_data'].empty_label='Select Data'
      