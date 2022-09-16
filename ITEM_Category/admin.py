from django.contrib import admin
from .models import Category_Model
# Register your models here.
@admin.register(Category_Model)
class Categoryadmin(admin.ModelAdmin):
    list_display= ['Category_Name',
                  'Category_Description', 
                   'Created_By',
                  'Remark',
                  'HSN_Code',
        ]