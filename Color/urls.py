from django.urls import path
from Color import views

urlpatterns = [
    path('form',views.Color_forms,name='color-form'),
    path('color-list',views.list,name='color-list'),
    path('edit/<int:Color_Code>/',views.color_edit_form,name='edit'),
    path('color-list/search',views.Search_Color,name='searchcolor'),
    path('delete/<int:Color_Code>/',views.Color_Delete,name='delete'), 
]
