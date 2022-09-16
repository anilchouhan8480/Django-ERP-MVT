
from django import forms
from django.forms.widgets import TextInput
from .models import Customer_models


class Customer_Forms(forms.ModelForm):
    class Meta:
        model = Customer_models
        fields =['Customer_Code_Display','Name','Email','Mobile_NO','GSTIN','Place_Of_Supply','title',
                 'Billing_Name','Street_h_n','City','state','postalcode','country','Name_shipping',
                 'Street_h_n_ship','City_ship','state_ship','postalcode_ship','country_ship','Remark',
                    'title_ship']

        labels={
    'Mobile_NO':'Mobile Number',
    'Street_h_n':'Street/House No.',
    'postalcode':'Postal Code',
    'title_ship':'Title',
    'Name_shipping':'Name',
    'Street_h_n_ship':'Street/House No.',
    'City_ship':'City',
    'state_ship':'State',
    'postalcode_ship':'Postal Code',
    'country_ship':'country',
    "Customer_Code_Display": "Customer Code",
    'Billing_Name':'Name'
}
        widgets={
            "Customer_Code_Display":TextInput(attrs={'disabled':'True'}), 
        }
    def __init__(self,*args,**kwargs):
        super(Customer_Forms,self).__init__(*args,**kwargs)
        self.fields['state'].empty_label='Select State'
        self.fields['state_ship'].empty_label='Select State'
        self.fields['Place_Of_Supply'].empty_label='Select State'