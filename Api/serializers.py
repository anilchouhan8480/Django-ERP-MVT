from ITEM_Category.models import Category_Model
from Item_Master.models import Item_Model
from rest_framework import serializers
from Supplier.models import Supplier_models
from Item_Master.models import Item_Model

class SupplierSerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(source='state.State_Name')

    class Meta:
        model = Supplier_models
        fields = [
            'Supplier_Code',
            'Name',
            'Email',
            'Mobile_NO',
            'Street_h_n',
            'City',
            'state_name',
            'Remark'
        ]

class ItemSerializer(serializers.ModelSerializer):
    color_name = serializers.CharField(source='Color.Color_Name')
    Item_GST = serializers.CharField(source='Item_GST.Gst')
    uom = serializers.CharField(source='UOM.UOM')

    class Meta:
        model = Item_Model
        fields = ['Item_NO', 'Item_Name', 'Created_By', 'Item_Description','uom',
                  'Item_Remark', 'Item_Category', 'Item_GST', 'Item_PCS', 'Item_Size','color_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Model
        fields = [
            'HSN_Code',
        ]
class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Model
        fields = '__all__'