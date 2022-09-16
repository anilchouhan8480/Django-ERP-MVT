from json import dumps

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from Item_Master.models import Item_Model
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Supplier.models import Supplier_models
from ITEM_Category.models import Category_Model
from .serializers import ItemSerializer, SupplierSerializer, CategorySerializer,ItemMasterSerializer

class SupplierModelViewSet(viewsets.ModelViewSet):
    queryset = Supplier_models.objects.all()
    serializer_class = SupplierSerializer

class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Item_Model.objects.all()
    serializer_class = ItemSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category_Model.objects.all()
    serializer_class = CategorySerializer

class ItemMasterModelViewSet(viewsets.ModelViewSet):
    queryset = Item_Model.objects.all()
    serializer_class = ItemMasterSerializer
