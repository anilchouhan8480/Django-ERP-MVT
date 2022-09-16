from rest_framework import serializers
from .models import Item_Model

# class SupplierSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Item_Model
# 		fields = ['Supplier_Code','Name','Email','Mobile_NO','GSTIN','Place_Of_Supply','title','Billing_Name','Street_h_n','City','state','postalcode','country','title_ship','Name_shipping','Street_h_n_ship','City_ship','state_ship','postalcode_ship','country_ship','Remark']