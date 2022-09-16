from operator import mod
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category_Model(models.Model):
    Category_NO = models.AutoField(primary_key=True)
    is_del = models.BooleanField(default=False)
    Category_Prefix = models.CharField(max_length=20,default='CAT0')
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Category_Name = models.CharField(max_length=25)
    HSN_Code = models.CharField(max_length=20)
    Category_Description = models.CharField(max_length=80)
    Created_Date = models.DateField(auto_now_add=True)
    Remark = models.CharField(max_length=100,blank=True,default=None)
    

    def __str__(self):
        return "%s" % (self.Category_Name)
        
    @property
    def Category_id(self):
        return f"{self.Category_Prefix}{self.Category_NO}"
   