from django import forms
from django.forms.widgets import TextInput
from .models import Category_Model



class Category_form(forms.ModelForm):
    class Meta:
        model = Category_Model
        fields = ['Category_Name',
                  'Category_Description',
                  'Created_By',
                  'Remark',
                  'HSN_Code',
        ]

        widgets = {
            'Category_Name':TextInput(attrs={'placeholder':"Enter Category Name"}),
            'Category_Description':TextInput(attrs={'placeholder':"Enter Description"}),
            
                }
