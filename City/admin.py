from django.contrib import admin
from .models import City_Model
# Register your models here.
@admin.register(City_Model)
class City_Admin(admin.ModelAdmin):
    list_display=['City_Code','City_Name','Remark','Created_By', 'Created_Date',
    ]