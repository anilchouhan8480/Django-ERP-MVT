from django.db import models
from django.contrib.auth.models import User

class TallyModel(models.Model):
    Tally_NO = models.AutoField(primary_key=True)
    Data_Name = models.CharField(max_length=200,blank=True, null=True)
    Tally_Prefix = models.CharField(max_length=20,default='TAL0')
    is_del = models.BooleanField(default=False)
    Transection_No = models.CharField(max_length=50,blank=True, null=True)
    Tally_Name = models.CharField(max_length=50)
    Created_Date = models.DateField(auto_now_add=True)
    Created_By = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    Remark = models.CharField(max_length=100,blank=True,default=None)


    def __str__(self):
        return "%s" % (self.Data_Name)

    @property
    def Tally_master_id(self):
        return f"{self.Tally_Prefix}{self.Tally_NO}"