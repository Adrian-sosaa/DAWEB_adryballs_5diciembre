from django.db import models

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(null=False, primary_key=True)
    num_empleados = models.IntegerField(null=False)
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=200, null=False)
    productos = models.CharField(max_length=200, null=False)
    numero_productos = models.IntegerField(null=False)
    Telefono = models.IntegerField(null=False)