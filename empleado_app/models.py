from django.db import models

class Empleado(models.Model):
    id_empleado = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    curp = models.CharField(max_length=20, null=False)
    Telefono = models.IntegerField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=20, null=False)
    id_sucursal = models.CharField(max_length=20, null=False)
    feching = models.DateField(null=False)