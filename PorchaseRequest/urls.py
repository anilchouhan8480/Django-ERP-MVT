from django.urls import path
from . import views

urlpatterns = [
    path('purchase_request', views.Purchase_request, name='purchase_request'),
    path('pr-list', views.pr_list, name='pr-list'),
    path('search/',views.Search_PR,name='searchpr'),
    path('edit/<int:PR_No>/', views.Edit_pr, name="edit_pr"),
    path('delete/<int:PR_meterial_id>/',views.PR_Delete,name='delete')  
]
