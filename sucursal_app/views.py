from django.shortcuts import render, redirect
from .models import Sucursal

def inicio_vistaSucursales(request):
    lasSucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursales.html", {"misSucursales": lasSucursales})

def registrarSucursal(request):
    id_sucursal = request.POST["numId_sucursal"]
    num_empleados = request.POST["numEmpleados"]
    nombre = request.POST["txtNombre"]
    direccion = request.POST["txtDireccion"]
    productos = request.POST["txtProductos"]
    numero_productos = request.POST["numNumero_productos"]
    Telefono = request.POST["numTelefono"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal,
        num_empleados=num_empleados,
        nombre=nombre,
        direccion=direccion,
        productos=productos,
        numero_productos=numero_productos,
        Telefono=Telefono,
    )

    return redirect("sucursales")

def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursales.html", {"misSucursales": sucursal})

def editarSucursal(request):
    id_sucursal = request.POST["numId_sucursal"]
    num_empleados = request.POST["numEmpleados"]
    nombre = request.POST["txtNombre"]
    direccion = request.POST["txtDireccion"]
    productos = request.POST["txtProductos"]
    numero_productos = request.POST["numNumero_productos"]
    Telefono = request.POST["numTelefono"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.num_empleados = num_empleados
    sucursal.nombre = nombre
    sucursal.direccion = direccion
    sucursal.productos = productos
    sucursal.numero_productos = numero_productos
    sucursal.Telefono = Telefono
    sucursal.save()

    return redirect("sucursales")

def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursales")
