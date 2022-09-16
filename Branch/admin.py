from django.contrib import admin
from . models import Branch_model

# Register your models here.
@admin.register(Branch_model)
class Branch_Admin(admin.ModelAdmin):
    list_display=['Branch_Name','Mobile_NO', 'Branch_add',
                  'City','state','Remark',
                ]
