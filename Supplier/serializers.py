from rest_framework import serializers
from .models import Supplier_models
from Item_Master.models import Item_Model


class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supplier_models
    fields = ['Supplier_Code','Name','Email','Mobile_NO','GSTIN','Place_Of_Supply','title','Billing_Name','Street_h_n','City','state','postalcode','country','title_ship','Name_shipping','Street_h_n_ship','City_ship','state_ship','postalcode_ship','country_ship','Remark']



class ItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = Item_Model
    fields = ['Item_NO','Item_Name','Created_By','HSN_Code','Item_Description', 'Item_Remark','Item_Category','Item_GST','Item_PCS','Item_Size','Item_Colour']