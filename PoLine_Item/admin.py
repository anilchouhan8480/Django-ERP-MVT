from django.contrib import admin
from .models import PoLine_Model
# Register your models here.
@admin.register(PoLine_Model)
class PoLine_Admin(admin.ModelAdmin):
    list_display=['PoLine_Code','PoLine_No','Remark','Created_By', 'Created_Date',]