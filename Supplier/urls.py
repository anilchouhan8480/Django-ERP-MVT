from django.urls import path

from Supplier import views

urlpatterns = [
    path('supplier_create', views.Supplier_add_form, name='supplier-Form'),
    path('supplier-list', views.Supplier_list, name='supplier-list'),
    path('edit/<int:Supplier_Code>/', views.edit_sup_form, name='editsup'),
    path('search/', views.Search_Supplier, name='searchsup'),
    path('delete/<int:Supplier_Code>/', views.Supplier_Delete, name='delete'),
    path('supplier_details/<int:Supplier_Code>/', views.details, name='supplier_details'),
]
