from django.db import models
from django_countries.fields import CountryField
from State.models import State_Model
title_choice = [
    ('MR.','MR.'),
    ('MS.','MS.'),
    ('MRS.','MRS.'),
]
class Supplier_models(models.Model):
    Supplier_Code =models.AutoField(primary_key=True)
    Name = models.CharField(max_length=25)
    supplier_prefix = models.CharField(max_length=20,default='SUP0')
    is_del = models.BooleanField(default=False)
    Email = models.EmailField()
    Mobile_NO = models.BigIntegerField()
    GSTIN = models.CharField(max_length=25,blank=True,null=True)
    Place_Of_Supply =models.ForeignKey(State_Model,related_name='State_s', on_delete=models.CASCADE)
    suppliers_product = models.CharField(max_length=25,blank=True,null=True)
    title = models.CharField(max_length=25,choices=title_choice,default=title_choice[0])
    Billing_Name = models.CharField(max_length=50)
    Street_h_n = models.CharField(max_length=50,blank=True,null=True)
    City = models.CharField(max_length=50,blank=True,null=True)
    state = models.ForeignKey(State_Model, on_delete=models.CASCADE)
    postalcode = models.IntegerField(blank=True,null=True)
    country= CountryField(blank_label='Select country')
    Remark=models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return "%s" % (self.Name)
    @property
    def Supplier_id(self):
        return f"{self.supplier_prefix}{self.Supplier_Code}"