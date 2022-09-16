from django.contrib import admin
from .models import State_Model
# Register your models here.
@admin.register(State_Model)
class State_Admin(admin.ModelAdmin):
    list_display=['State_Code','State_Name','Remark','Created_By', 'Created_Date',]