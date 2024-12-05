from django.db import models

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cant_producto = models.IntegerField(null=False)
    calidad = models.CharField(max_length=50, null=False)
    id_sucursal = models.IntegerField(max_length=50, null=False)
    id_prov = models.IntegerField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    tipobalon = models.CharField(max_length=50, null=False)
