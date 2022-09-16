from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r'supplierapi', views.SupplierModelViewSet,basename='supplierapi'),
router.register(r'itemapi', views.ItemModelViewSet, basename='itemapi'),
router.register(r'Categoryapi', views.CategoryModelViewSet, basename='Categoryapi'),
router.register(r'ItemMasterapi', views.ItemMasterModelViewSet, basename='ItemMasterapi'),

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
