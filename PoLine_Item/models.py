from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PoLine_Model(models.Model):
    PoLine_Code = models.AutoField(primary_key=True)
    is_del = models.BooleanField(default=False)
    PoLine_Prefix = models.CharField(max_length=20,default='PLT0')
    PoLine_No= models.CharField(max_length=50)
    Description = models.CharField(max_length=100,blank=True)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Remark = models.CharField(max_length=100,blank=True,default=None)
    
    @property
    def  PoLine_Code(self):
        return f"{self. PoLine_Prefix}{self.PoLine_No}"

    def __str__(self):
        return "%s" % (self. PoLine_No)