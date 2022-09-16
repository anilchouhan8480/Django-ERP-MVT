from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Department_model(models.Model):
    Department_Code = models.AutoField(primary_key=True)
    Department_Prefix = models.CharField(max_length=20,default='DPM0')
    is_del = models.BooleanField(default=False)
    Department_Name = models.CharField(max_length=255)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Description = models.CharField(max_length=100)
    Remark = models.CharField(max_length=90,blank=True,default=None )
   
   
    def __str__(self):
        return "%s" % (self.Department_Name)
    
    @property
    def Department_id(self):
        return f"{self.Department_Prefix}{self.Department_Code}"
   


 