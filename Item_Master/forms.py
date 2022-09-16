from django import forms
from django.forms.widgets import TextInput
from .models import Item_Model



class Item_form(forms.ModelForm):
    class Meta:
        model = Item_Model
        fields = ['Item_NO','Item_Name','Created_By',
                  'Item_Description', 'Item_Remark',
                  'Item_Category','Item_GST',
                  'Item_PCS','Item_Pirce','Item_Size',
                  'Color','Item_Image',
                  'Item_Image_2','Item_Image_3',
                  'Item_Image_4','UOM',
        ]
       
        labels={
                    'Item_NO':'Item Id',
                    'Item_Size':'Size',
                    'Item_Category':'Category',
                    'Item_GST':'GST',
                    'Item_Description': 'Description',
                     'Item_PCS':'Pieces',
                     'Item_Pirce':'Price',
                      'Item_Image':'Image',
                        'Item_Image_2':'Image',
                        'Item_Image_3':'Image',
                        'Item_Image_4':'Image',
                }
        
        widgets = {
            'Item_Name':TextInput(attrs={'placeholder':'Enter Item'}),
            'Item_Size':TextInput(attrs={'placeholder':"Enter Size"}),
            'Item_Description':TextInput(attrs={'placeholder':"Enter Description"}),
            'Item_Remark':TextInput(attrs={'placeholder':"Enter Remark"}),
            'Item_PCS':TextInput(attrs={'placeholder':"Enter Pieces"}),
            'Item_Pirce':TextInput(attrs={'placeholder':"Enter Pieces"}),
                }
      
        
        
    def __init__(self,*args,**kwargs):
        super(Item_form,self).__init__(*args,**kwargs)
        self.fields['Item_Category'].empty_label='Select'
        self.fields['Item_GST'].empty_label='Select GST'
        self.fields['Color'].empty_label='Select Color'
        self.fields['UOM'].empty_label='Select UOM'
     
    
   