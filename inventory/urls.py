from django.urls import path

from inventory import views

urlpatterns = [
    path('inventory-list', views.inventory_list, name='inventory-list'),
    path('stock-details', views.stock_details, name='stock-details'),
    path('stock-details-create', views.stock_details_create, name='stock-details-create'),


    path('stock-history', views.stock_history, name='stock-history'),
    

]
