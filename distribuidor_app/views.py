from django.shortcuts import render, redirect
from .models import Distribuidor

def inicio_vistaDistribuidores(request):
    losDistribuidores = Distribuidor.objects.all()
    return render(request, "gestionarDistribuidores.html", {"misDistribuidores": losDistribuidores})

def registrarDistribuidor(request):
    id_distribuidor = request.POST["numId_distribuidor"]
    nombre = request.POST["txtNombre"]
    telefono = request.POST["numTelefono"]
    productos = request.POST["txtProductos"]
    direccion = request.POST["txtDireccion"]
    nie = request.POST["numNie"]
    cant_producto = request.POST["txtCantProducto"]

    Distribuidor.objects.create(
        id_distribuidor=id_distribuidor,
        nombre=nombre,
        telefono=telefono,
        productos=productos,
        direccion=direccion,
        nie=nie,
        cant_producto=cant_producto,
    )

    return redirect("distribuidores")

def seleccionarDistribuidor(request, id_distribuidor):
    distribuidor = Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    return render(request, "editarDistribuidores.html", {"misDistribuidores": distribuidor})

def editarDistribuidor(request):
    id_distribuidor = request.POST["numId_distribuidor"]
    nombre = request.POST["txtNombre"]
    telefono = request.POST["numTelefono"]
    productos = request.POST["txtProductos"]
    direccion = request.POST["txtDireccion"]
    nie = request.POST["numNie"]
    cant_producto = request.POST["txtCantProducto"]

    distribuidor = Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    distribuidor.nombre = nombre
    distribuidor.telefono = telefono
    distribuidor.productos = productos
    distribuidor.direccion = direccion
    distribuidor.nie = nie
    distribuidor.cant_producto = cant_producto
    distribuidor.save()

    return redirect("distribuidores")

def borrarDistribuidor(request, id_distribuidor):
    distribuidor = Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    distribuidor.delete()
    return redirect("distribuidores")
