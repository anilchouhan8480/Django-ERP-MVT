from django.contrib import admin
from .models import Gst_Model
# Register your models here.
@admin.register(Gst_Model)
class Gst_Admin(admin.ModelAdmin):
    list_display=['Gst_Code','Description','Gst','Created_By']