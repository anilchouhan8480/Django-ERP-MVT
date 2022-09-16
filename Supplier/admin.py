from django.contrib import admin
from . models import Supplier_models
# Register your models here.
@admin.register(Supplier_models)
class Supplier_admin(admin.ModelAdmin):
    list_display=['Supplier_Code','Name','Email','Mobile_NO','GSTIN','Place_Of_Supply',
                'title','Billing_Name','Street_h_n','City','state','postalcode','country','Remark','suppliers_product']
