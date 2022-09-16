from django.urls import path
from State import views

urlpatterns = [
   path('form',views.state_Form,name='state-form'),
    path('state-list',views.State_list,name='state-list'),
    path('edit/<int:State_Code>/',views.State_edit_form,name='edit'),
    path('search/',views.search_State,name='search_state'),
    path('delete/<int:State_Code>/',views.State_Delete,name='delete'), 
]
