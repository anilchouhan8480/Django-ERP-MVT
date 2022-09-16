from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class State_Model(models.Model):
    State_Code = models.AutoField(primary_key=True)
    State_Prefix = models.CharField(max_length=20,default='STE0')
    is_del = models.BooleanField(default=False)
    State_Name = models.CharField(max_length=50)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Remark = models.CharField(max_length=100,blank=True,default=None)
    
    @property
    def State_id(self):
        return f"{self.State_Prefix}{self.State_Code}"

    def __str__(self):
        return "%s" % (self.State_Name)
    
    