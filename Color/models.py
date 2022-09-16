from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Color_Model(models.Model):
    Color_Code = models.AutoField(primary_key=True)
    Color_Prefix = models.CharField(max_length=20,default='COL0')
    is_del = models.BooleanField(default=False)
    Color_Name = models.CharField(max_length=50)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Remark = models.CharField(max_length=90,blank=True,default=None)
      
   
    def __str__(self):
        return "%s" % (self.Color_Name)
    
    @property
    def Color_id(self):
        return f"{self.Color_Prefix}{self.Color_Code}"
   
  