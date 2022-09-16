from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City_Model(models.Model):
    City_Code = models.AutoField(primary_key=True)
    City_Prefix = models.CharField(max_length=20,default='CT00')
    is_del = models.BooleanField(default=False)
    City_Name = models.CharField(max_length=50)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Remark = models.CharField(max_length=100,blank=True,default=None)
   
    def __str__(self):
        return "%s" % (self.City_Name)
        
    @property
    def City_id(self):
        return f"{self.City_Prefix}{self.City_Code}"
    
   
    