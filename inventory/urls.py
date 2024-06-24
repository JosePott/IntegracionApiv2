from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'proveedores', views.ProveedorViewSet)
router.register(r'ubicaciones', views.UbicacionViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'inventarios', views.InventarioViewSet)
router.register(r'recepciones', views.RecepcionViewSet)
router.register(r'devoluciones', views.DevolucionViewSet)
router.register(r'ordenes-compra', views.OrdenCompraViewSet)
router.register(r'detalles-ordenes-compra', views.DetalleOrdenCompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
