from django.contrib import admin
from .models import Item_Model


# Register your models here.
@admin.register(Item_Model)
class Item_Admin(admin.ModelAdmin):
    list_display= ['Item_Name','Created_Date','Created_By',
                   'Last_Change_Date',
                   'Item_Description','Item_Remark','Item_Category',
                   'Item_GST','Item_PCS','Item_Size','Color','UOM',
                #    'Item_Image','Item_Image_2','Item_Image_3','Item_Image_4'
    ]
   
