from django.urls import path
from Item_Master import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ('item_create',views.item_add_form,name='Item-Form'),
    path('item-list/',views.item_list,name='item-list'),
    path('item-list/edit/<int:Item_NO>/',views.edit_form,name='edit'),
    path('item-list/search',views.Search_Item,name='searchitem'),
    path('item-list/delete/<int:Item_NO>/',views.Item_Delete,name='delete')
     
]+static (settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) # +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
