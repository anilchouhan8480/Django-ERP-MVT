from django.urls import  path
from UOM import views
urlpatterns=[
    
    path('form',views.UOM_forms,name='UOMform'),
    path('uom-list',views.list,name='unitofmeasure-list'),
    path('edit/<int:UOM_NO>/',views.uom_edit_form,name='edit'),
    path('uom-list/search',views.Search_UOM,name='searchuom'),
    path('delete/<int:UOM_NO>/',views.UOM_Delete,name='delete')    
]
