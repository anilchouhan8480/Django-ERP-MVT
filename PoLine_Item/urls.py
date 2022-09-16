from django.urls import path
from PoLine_Item import views

urlpatterns = [
    path('form',views.poLine_Form,name='poLine-form'),
    path('PoLine-list',views.PoLine_list,name='PoLine-list'),
    path('edit/<int:PoLine_No>/',views.PoLine_edit_form,name='edit'),
    path('PoLine-list/search',views.search_PoLine,name='searchpoline'),
    path('delete/<int:PoLine_Code>/',views.PoLine_Delete,name='delete'), 
]
