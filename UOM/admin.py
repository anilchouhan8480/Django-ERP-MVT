from django.contrib import admin
from . models import UOM_model

# Register your models here.
@admin.register(UOM_model)
class UOMAdmin(admin.ModelAdmin):
    list_display= ['UOM','Created_Date','Created_By',
                'Description','Remark',
                   
    ]
   