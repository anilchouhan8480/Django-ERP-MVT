from django import forms
from django.db import models
from django_countries.fields import CountryField
from State.models import State_Model
# Create your models here.

title_choice = [
    ('MR.','MR.'),
    ('MS.','MS.'),
    ('MRS.','MRS.'),
]
class Customer_models(models.Model):
    Customer_Code =models.AutoField(primary_key=True)
    Name = models.CharField(max_length=25)
    Customer_Code_Display = models.IntegerField(null=True,blank=True)
    customer_prefix = models.CharField(max_length=20,default='CUS0')
    is_del = models.BooleanField(default=False)
    Email = models.EmailField()
    Mobile_NO = models.BigIntegerField()
    GSTIN = models.CharField(max_length=25,blank=True)
    Place_Of_Supply =models.ForeignKey(State_Model,related_name='State_Mod', on_delete=models.CASCADE)
    title = models.CharField(max_length=25,choices=title_choice,default=title_choice[0],blank=True,null=True)
    Billing_Name = models.CharField(max_length=50,blank=True)
    Street_h_n = models.CharField(max_length=50,blank=True)
    City = models.CharField(max_length=50,blank=True)
    state = models.ForeignKey(State_Model, on_delete=models.CASCADE)
    postalcode = models.IntegerField(blank=True)
    country =  CountryField(blank_label='Select country')
    Name_shipping = models.CharField(max_length=50,blank=True)
    title_ship=models.CharField(max_length=50,blank=True,choices=title_choice,default=title_choice[0],null=True)
    Street_h_n_ship = models.CharField(max_length=50,blank=True)
    City_ship=models.CharField(max_length=50,blank=True)
    state_ship=models.ForeignKey(State_Model,related_name='State_Model', on_delete=models.CASCADE)
    postalcode_ship=models.IntegerField(blank=True)
    country_ship =  CountryField(blank_label='Select country')
    Remark =models.CharField(max_length=50,blank=True,default=None)
    
    @property
    def Customer_id(self):
        return f"{self.customer_prefix}{self.Customer_Code}"
    
    def save(self, *args, **kwargs):
        self.Customer_Code_Display = self.Customer_Code
        super().save(*args, **kwargs)
        self.Customer_Code_Display = self.Customer_Code
        super().save(*args, **kwargs)