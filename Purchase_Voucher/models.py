from datetime import datetime
from django.db import models
from Supplier.models import Supplier_models
from Tally_master.models import TallyModel

payment_type=[
    ('Cash','Cash'),
    ('Check','Check'),
    ('UPI','UPI'),
   ( 'Net-Banking','Net-Banking'),
   ('PhonePay','PhonePay'),
   ('Gpay','Gpay')

]


# Create your models here.
class Payment_vouchers(models.Model):
    Payment_NO = models.AutoField(primary_key=True)
    Payment_Prefix = models.CharField(max_length=20,default='PMT0')
    Supplier_Name = models.ForeignKey(Supplier_models,on_delete=models.CASCADE)
    Tally_data = models.ForeignKey(TallyModel,related_name='tally',on_delete=models.CASCADE)
    is_del = models.BooleanField(default=False)
    Payment_amount = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=80,choices=payment_type)
    Transection_No = models.CharField(max_length=100)
    Bill_No = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    payment_date = models.DateField(blank=True, null=True)


    @property
    def Payment_id(self):
        return f"{self.Payment_Prefix}{self.Payment_NO}"
   