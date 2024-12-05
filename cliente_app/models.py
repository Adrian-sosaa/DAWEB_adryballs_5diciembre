from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(null=False, primary_key=True)
    direccion = models.CharField(max_length=100, null=False)
    nombre = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    numero_productos_adquiridos = models.IntegerField(null=False)
    tipo_de_pago = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField(null=False)