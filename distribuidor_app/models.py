from django.db import models

class Distribuidor(models.Model):
    id_distribuidor = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    productos = models.CharField(max_length=200, null=False)
    direccion = models.CharField(max_length=100, null=False)
    nie = models.IntegerField(null=False)
    cant_producto = models.IntegerField(null=False)