from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from LoginApp import views as userView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include('Item_Master.urls')),
    path('supplier/', include('Supplier.urls')),
    path('customer/', include('Customer.urls')),
    path('uom/', include('UOM.urls')),
    path('gst/', include('GST.urls')),
    path('department/', include('Department.urls')),
    path('Category/', include('ITEM_Category.urls')),
    path('state/', include('State.urls')),
    path('pr/', include('PorchaseRequest.urls')),
    path('po/', include('PorchaseOrder.urls')),
    path('api/', include('Api.urls')),
    path('branch/', include('Branch.urls')),
    path('city/', include('City.urls')),
    path('color/', include('Color.urls')),
    path('', include('LoginApp.urls')),
    path('poline/', include('PoLine_Item.urls')),
    path('pv/', include('Purchase_Voucher.urls')),
    path('dashboard/logout/', userView.logout_call, name='logout'),
    path('inventory/', include('inventory.urls')),
    path('tally/', include('Tally_master.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
