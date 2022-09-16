from django.urls import path

from . import views

urlpatterns = [
    path('purchase_order', views.Purchase_order, name='purchase_order'),
    path('purchase-list', views.purchase_list, name='purchase-list'),
    path('search/',views.Search_PO,name='searchpo'),
    path('edit/<int:PO_No>/', views.Edit_po, name="edit_po"),
    path('delete/<int:PO_No>/',views.PO_Delete,name='delete') ,
    path('print/<int:PO_No>/', views.get_print_data, name='print'),   
    path('print/', views.get_print_data, name='print'),
]

