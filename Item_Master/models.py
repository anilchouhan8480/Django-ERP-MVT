from operator import mod
from django.db import models
from ITEM_Category.models import Category_Model
from GST.models import  Gst_Model
from Color.models import Color_Model
from UOM.models import UOM_model
from django.contrib.auth.models import User
# Create your models here.
class Item_Model(models.Model):
    Item_NO = models.AutoField(primary_key=True)
    is_del = models.BooleanField(default=False)
    Item_Prefix = models.CharField(max_length=20,default='ITM0')
    Item_Name = models.CharField(max_length=25)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Last_Change_Date= models.DateTimeField(auto_now_add=True)
    Item_Description = models.CharField(max_length=100)
    Item_Remark = models.CharField(max_length=100,blank=True,default=None)
    Item_Category = models.ForeignKey(Category_Model,on_delete=models.CASCADE)
    Item_GST = models.ForeignKey(Gst_Model,on_delete=models.CASCADE)
    Item_PCS = models.CharField(max_length=20)
    Item_Size = models.CharField(max_length=20)
    Color =models.ForeignKey(Color_Model,on_delete=models.CASCADE)
    UOM= models.ForeignKey(UOM_model,on_delete=models.CASCADE)
    Item_Pirce = models.IntegerField()
    Item_Image = models.ImageField(upload_to='images',blank=True,null=True)
    Item_Image_2 = models.ImageField(upload_to='images',blank=True,null=True)
    Item_Image_3 = models.ImageField(upload_to='images',blank=True,null=True)
    Item_Image_4 = models.ImageField(upload_to='images',blank=True,null=True)
  
    @property
    def Item_id(self):
        return f"{self.Item_Prefix}{self.Item_NO}"

