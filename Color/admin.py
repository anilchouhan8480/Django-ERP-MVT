from django.contrib import admin
from .models import Color_Model

# Register your models here.

@admin.register(Color_Model)
class Color_Admin(admin.ModelAdmin):
    list_display=['Color_Code','Color_Name','Remark',
                    'Created_Date','Created_By',
    ]