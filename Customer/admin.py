from django.contrib import admin
from . models import Customer_models
# Register your models here.
@admin.register(Customer_models)
class Customer_admin(admin.ModelAdmin):
    list_display=['Name','Email','Mobile_NO',
                  'GSTIN','Place_Of_Supply','title','Billing_Name','Street_h_n',
                  'City','state','postalcode','country','Name_shipping','Street_h_n_ship',
                  'City_ship','state_ship','postalcode_ship','country_ship','Remark']
