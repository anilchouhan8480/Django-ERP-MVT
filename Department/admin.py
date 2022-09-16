from django.contrib import admin
from . models import Department_model

# Register your models here.
@admin.register(Department_model)
class DepartmentAdmin(admin.ModelAdmin):
    list_display= ['Department_Code','Department_Name','Created_Date','Created_By',
                'Description','Remark',
                   
    ]
   