from django.urls import path
from Customer import views
urlpatterns = [
    path ('customer_create',views.Customer_add_form,name='customer-Form'),
    path('customer-list/',views.Customer_list,name='customer-list'),
    path('customer-list/edit/<int:Customer_Code>',views.edit_cs_form,name='edit'),
    path('customer-list/search/',views.Search_Customer,name='search'),
    path('customer-list/delete/<int:Customer_Code>/',views.Customer_Delete,name='delete')
]