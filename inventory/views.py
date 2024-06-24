from rest_framework import viewsets, status
from .models import Proveedor, Ubicacion, Producto, Inventario, Recepcion, Devolucion, OrdenCompra, DetalleOrdenCompra
from .serializers import ProveedorSerializer, UbicacionSerializer, ProductoSerializer, InventarioSerializer, RecepcionSerializer, DevolucionSerializer, OrdenCompraSerializer, DetalleOrdenCompraSerializer
from rest_framework.response import Response

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class RecepcionViewSet(viewsets.ModelViewSet):
    queryset = Recepcion.objects.all()
    serializer_class = RecepcionSerializer

class DevolucionViewSet(viewsets.ModelViewSet):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Actualizar el inventario
        devolucion = serializer.instance
        try:
            inventario = Inventario.objects.get(producto=devolucion.producto)
            inventario.cantidad_disponible += devolucion.cantidad_devuelta
            inventario.save()
        except Inventario.DoesNotExist:
            # Manejar el caso en que no exista el inventario para el producto devuelto
            return Response({'error': 'No existe el inventario para el producto devuelto.'}, status=status.HTTP_400_BAD_REQUEST)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OrdenCompraViewSet(viewsets.ModelViewSet):
    queryset = OrdenCompra.objects.all()
    serializer_class = OrdenCompraSerializer

class DetalleOrdenCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrdenCompra.objects.all()
    serializer_class = DetalleOrdenCompraSerializer
