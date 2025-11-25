from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Movimiento(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
