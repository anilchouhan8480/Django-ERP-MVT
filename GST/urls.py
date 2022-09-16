from django.urls import path
from GST import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('form',views.gst_forms,name='gst-form'),
    path('gst-list',views.list,name='gst-list'),
    path('edit/<int:Gst_Code>/',views.gst_edit_form,name='edit'),
    path('gst-list/search',views.search_GST,name='searchgst'),
    path('delete/<int:Gst_Code>/',views.gst_Delete,name='delete')    

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
