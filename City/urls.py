from django.urls import path
from City import views

urlpatterns = [
    path('form',views.City_forms,name='city-form'),
    path('city-list',views.list,name='city-list'),
    path('edit/<int:City_Code>/',views.City_edit_form,name='edit'),
    path('city-list/search',views.Search_City,name='searchcityy'),
    path('delete/<int:City_Code>/',views.City_Delete,name='delete'), 
]
