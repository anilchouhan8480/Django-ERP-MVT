from django.urls import path
from ITEM_Category import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('form',views.category_forms,name='category-form'),
    path('category-list',views.list,name='category-list'),
    path('edit/<int:Category_NO>/',views.category_edit_form,name='edit'),
    path('category-list/search',views.Search_Category,name='searchcat'),
    path('delete/<int:Category_NO>/',views.Category_Delete,name='delete')    

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
