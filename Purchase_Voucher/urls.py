from django.urls import path
from Purchase_Voucher import views
urlpatterns = [
    path('forms',views.PVoucher_forms,name="voucher-form"),
    path('voucher-list',views.list,name='voucher-list'),
    path('ledger-list',views.ledger_list,name='ledger-list'),
    path('edit/<int:Payment_NO>/',views.voucher_edit_form,name='edit'),
    path('voucher-list/search',views.Search_voucher,name='Searchvoucher'),
    path('delete/<int:Payment_NO>/',views.Voucher_Delete,name='delete'),
    path('ledger-list/search',views.Search_ledger,name='Searchledger'),
    path('invoice',views.invoice,name='invoice'),
    path('print/<int:Voucher_NO>/',views.get_print_data,name='print'),   
    path('print/',views.get_print_data,name='print'),

]


