from django.db import models

class Venta(models.Model):
    id_venta = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    hora_compra = models.TimeField(null=False)
    contenido = models.CharField(max_length=200, null=False)
    cantidad = models.IntegerField(null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    reg_final= models.DateField( null=False)
    nom_cliente = models.CharField(max_length=50, null=False)
    id_cliente = models.IntegerField(null=False)
    id_empleado = models.IntegerField(null=False)
    id_producto = models.IntegerField(null=False)
    id_sucursal = models.IntegerField(null=False)
