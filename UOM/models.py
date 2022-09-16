from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UOM_model(models.Model):
    UOM_NO = models.AutoField(primary_key=True)
    is_del = models.BooleanField(default=False)
    UMO_Prefix = models.CharField(max_length=20, default='UOM0')
    UOM = models.CharField(max_length=200)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Description = models.CharField(max_length=100)
    Remark = models.CharField(max_length=90,blank=True,default=None)
   
    def __str__(self):
        return self.UOM
    @property
    def UOM_id(self):
        return f"{self.UMO_Prefix }{self.UOM_NO}"
    
   