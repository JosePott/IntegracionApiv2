from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    contacto_principal = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_expiracion = models.DateField(null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    fecha_ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad_disponible}'

class Recepcion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_recibida = models.IntegerField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    verificado_por = models.CharField(max_length=100)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad_recibida}'

class Devolucion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_devuelta = models.IntegerField()
    fecha_devolucion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=255)
    procesado_por = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad_devuelta}'

class OrdenCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.proveedor.nombre} - {self.fecha_orden}'

class DetalleOrdenCompra(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.orden_compra.id} - {self.producto.nombre}'