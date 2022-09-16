from django.urls import path
from Department import views
urlpatterns=[
    path('form',views.Department_forms,name='Departmentform'),
    path('dep-list',views.list,name='department-list'),
    path('edit/<int:Department_Code>/',views.department_edit_form,name='edit'),
    path('department-list/search',views.Search_dep,name='searchdep'),
    path('delete/<int:Department_Code>/',views.dep_Delete,name='delete')       
]

 

