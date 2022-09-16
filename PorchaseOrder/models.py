from django.db import models
from Supplier.models import Supplier_models
from Item_Master.models import Item_Model
from django.utils.crypto import get_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User


# Create your models here.
class PurchaseOrder(models.Model):
    PO_No = models.AutoField(primary_key=True)
    PO_Prefix = models.CharField(max_length=20,default='PO0')
    is_del= models.BooleanField(default=False)
    Supplier_Code = models.ForeignKey(to=Supplier_models, on_delete=models.CASCADE)
    Description= models.CharField(max_length=500,blank=True, null=True)
    PO_Status = models.CharField(max_length=100,blank=True, null=True)
    GST = models.CharField(max_length=200,blank=True, null=True)
    Gst_percent = models.CharField(max_length=20, default="9%")
    Location = models.CharField(max_length=100,blank=True, null=True)
    Expected_Arrival_date = models.DateField(blank=True, null=True)
    Item_count= models.CharField(max_length=50,blank=True, null=True)
    Remark= models.CharField(max_length=500,blank=True, null=True)
    Created_By = models.CharField(max_length=20,blank=True, null=True)
    Created_At = models.DateField(auto_now_add=True)
    Updated_At = models.DateField(blank=True, null=True)
    
    @property
    def PO_id(self):
        return f"{self.PO_Prefix}{self.PO_No}"
   
    class Meta:
        default_related_name = '+'

    def __str__(self):
        return str(self.PO_No)
    
   
class Puchase_oreder_meterial(models.Model):
    PO_meterial_id = models.AutoField(primary_key=True)
    Purchase_order= models.ForeignKey(to=PurchaseOrder, on_delete=models.CASCADE)
    Item_id= models.ForeignKey(Item_Model,related_name='item', on_delete=models.CASCADE)
    PO_line_Item = models.IntegerField(blank=True, null=True)
    Item_quantity = models.IntegerField(blank=True, null=True)
    Item_basePrice = models.DecimalField(max_digits = 10,decimal_places = 2,blank=True, null=True)
    Item_discount = models.IntegerField(blank=True, null=True, default='25')
    Gst_type = models.CharField(max_length=30,blank=True, null=True, default='CGST')
    Gst_percent = models.DecimalField(max_digits = 10,decimal_places = 2,blank=True, null=True)
    Total_Amount = models.DecimalField(max_digits = 10,decimal_places = 2,blank=True, null=True)
    Updated_At = models.DateField(blank=True, null=True)





