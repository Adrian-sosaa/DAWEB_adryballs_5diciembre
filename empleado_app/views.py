from django.shortcuts import render, redirect
from .models import Empleado

def inicio_vistaEmpleados(request):
    losEmpleados = Empleado.objects.all()
    return render(request, "gestionarEmpleados.html", {"misEmpleados": losEmpleados})

def registrarEmpleado(request):
    id_empleado = request.POST["numId_empleado"]
    nombre = request.POST["txtNombre"]
    curp = request.POST["txtCurp"]
    Telefono = request.POST["numTelefono"]
    direccion = request.POST["txtDireccion"]
    edad = request.POST["numEdad"]
    sexo = request.POST["txtSexo"]
    id_sucursal = request.POST["txtsucursal"]
    feching = request.POST["txtfechaentr"]

    Empleado.objects.create(
        id_empleado=id_empleado,
        nombre=nombre,
        curp=curp,
        Telefono=Telefono,
        direccion=direccion,
        edad=edad,
        sexo=sexo,
        id_sucursal=id_sucursal,
        feching=feching,
    )

    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleados.html", {"misEmpleados": empleado})

def editarEmpleado(request):
    id_empleado = request.POST["numId_empleado"]
    nombre = request.POST["txtNombre"]
    curp = request.POST["txtCurp"]
    Telefono = request.POST["numTelefono"]
    direccion = request.POST["txtDireccion"]
    edad = request.POST["numEdad"]
    sexo = request.POST["txtSexo"]
    id_sucursal = request.POST["txtsucursal"]
    feching = request.POST["txtfechaentr"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.curp = curp
    empleado.Telefono = Telefono
    empleado.direccion = direccion
    empleado.edad = edad
    empleado.sexo = sexo
    empleado.id_sucursal = id_sucursal
    empleado.feching=feching
    empleado.save()

    return redirect("empleados")

def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleados")
