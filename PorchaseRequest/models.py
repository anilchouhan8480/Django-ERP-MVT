from django.db import models
from Supplier.models import Supplier_models
from Item_Master.models import Item_Model
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied

# Create your models here.
class PurchaseRequest(models.Model):
    PR_No = models.AutoField(primary_key=True)
    PR_Prefix = models.CharField(max_length=20,default='PR0')
    PR_Status = models.CharField(max_length=100,blank=True, null=True)
    Supplier_Code = models.ForeignKey(Supplier_models, on_delete=models.CASCADE,related_name='supp_code')
    Description= models.CharField(max_length=500,default="None",blank=True, null=True)
    Requistioner = models.CharField(max_length=200,default="None")
    Item_Count= models.IntegerField()
    GST = models.CharField(max_length=200,blank=True, null=True)
    Location = models.CharField(max_length=100,blank=True, null=True)
    Gst_percent = models.CharField(max_length=20, default="9%")
    Expected_Arrival_date = models.DateField(blank=True, null=True)
    Remark= models.CharField(max_length=500,default="None",blank=True,null=True)
    Created_By = models.CharField(max_length=20,blank=True, null=True)
    Created_At = models.DateField(auto_now_add=True)
    Updated_By = models.CharField(max_length=20,blank=True, null=True)
    Updated_At = models.DateField(blank=True, null=True)

 
    @property
    def PR_id(self):
        return f"{self.PR_Prefix}{self.PR_No}"

class Puchase_request_meterial(models.Model):
  PR_meterial_id = models.AutoField(primary_key=True)
  Purchase_request= models.ForeignKey(PurchaseRequest, on_delete=models.CASCADE,related_name='puch_req')
  is_del= models.BooleanField(default="False")
  Item_id = models.ForeignKey(Item_Model, on_delete=models.CASCADE,related_name='itm_code')
  PR_line_Item = models.IntegerField(blank=True, null=True)
  Unit_Measure = models.CharField(max_length=50,blank=True, null=True)
  Item_quantity = models.IntegerField(default="10")
  Item_basePrice = models.DecimalField(max_digits = 10,decimal_places = 2,blank=True, null=True)
  Gst_type = models.CharField(max_length=20,blank=True, null=True)
  Gst_percent = models.DecimalField(max_digits = 10,decimal_places = 2,blank=True, null=True)
  Total_Amount= models.DecimalField(max_digits = 10,decimal_places = 2)
  Updated_At = models.DateField(blank=True, null=True)

