from django.contrib import admin
from .models import Payment_vouchers
# Register your models here.
@admin.register(Payment_vouchers)
class voucher_admin(admin.ModelAdmin):
    list_display=['Supplier_Name','Payment_amount','payment_type','Transection_No','description']