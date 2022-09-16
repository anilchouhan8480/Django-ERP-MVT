from django.db import models
from State.models import State_Model
from City.models import City_Model

# Create your models here.

class Branch_model(models.Model):
    Branch_Code = models.AutoField(primary_key=True)
    is_del = models.BooleanField(default=False)
    Branch_Name = models.CharField(max_length=25)
    Mobile_NO = models.BigIntegerField()
    Branch_add = models.CharField(max_length=50,blank=True)
    City = models.ForeignKey(City_Model, on_delete=models.CASCADE)
    state = models.ForeignKey(State_Model, on_delete=models.CASCADE)
    Remark = models.CharField(max_length=100,blank=True,default=None)

    def __str__(self):
        return "%s" % (self.Branch_Name)