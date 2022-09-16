from django.urls import path
from .import views

urlpatterns = [
    path('form',views.Tally_forms,name='tally-form'),
    path('tally-list',views.list,name='Tally-list'),
    path('edit/<int:Tally_NO>/',views.Tally_edit_form,name='edit'),
    path('tally-list/search',views.Search_Tally,name='searchtally'),
    path('delete/<int:Tally_NO>/',views.Tally_Delete,name='delete'),
]
