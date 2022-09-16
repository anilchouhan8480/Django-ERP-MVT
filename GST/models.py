from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gst_Model(models.Model):
    Gst_Code = models.AutoField(primary_key=True)
    Gst_Prefix = models.CharField(max_length=20,default='GST0')
    is_del = models.BooleanField(default=False)
    Description = models.CharField(max_length=50,blank=True)
    Gst = models.IntegerField(blank=True)
    Created_By =  models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
   
   
    def __str__(self):
        return "%s" % (self.Gst)
      
    @property
    def Gst_id(self):
        return f"{self.Gst_Prefix}{self.Gst_Code}"
   