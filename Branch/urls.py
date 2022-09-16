from django.urls import  path
from Branch import views

urlpatterns=[
    path('form',views.branch_Forms,name='Branch_Forms'),
    path('branch-list',views.list,name='Branch-list'),
    path('edit/<int:Branch_Code>/',views.branch_edit_form,name='edit'),
    path('branch-list/search',views.Search_Branch,name='searchbranch'),
    path('delete/<int:Branch_Code>/',views.Branch_Delete,name='delete')    
]
