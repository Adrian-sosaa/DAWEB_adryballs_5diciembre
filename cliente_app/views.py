from django.shortcuts import render, redirect
from .models import Cliente

def inicio_vistaClientes(request):
    losClientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misClientes": losClientes})

def registrarCliente(request):
    id_cliente = request.POST["numId_cliente"]
    direccion = request.POST["txtDireccion"]
    nombre = request.POST["txtNombre"]
    telefono = request.POST["numTelefono"]
    numero_productos_adquiridos = request.POST["numProductos"]
    tipo_de_pago = request.POST["txtTipoPago"]
    fecha_nac = request.POST["txtFechaNac"]

    Cliente.objects.create(
        id_cliente=id_cliente,
        direccion=direccion,
        nombre=nombre,
        telefono=telefono,
        numero_productos_adquiridos=numero_productos_adquiridos,
        tipo_de_pago=tipo_de_pago,
        fecha_nac=fecha_nac,
    )

    return redirect("clientes")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html", {"misClientes": cliente})

def editarCliente(request):
    id_cliente = request.POST["numId_cliente"]
    direccion = request.POST["txtDireccion"]
    nombre = request.POST["txtNombre"]
    telefono = request.POST["numTelefono"]
    numero_productos_adquiridos = request.POST["numProductos"]
    tipo_de_pago = request.POST["txtTipoPago"]
    fecha_nac = request.POST["txtFechaNac"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.direccion = direccion
    cliente.nombre = nombre
    cliente.telefono = telefono
    cliente.numero_productos_adquiridos = numero_productos_adquiridos
    cliente.tipo_de_pago = tipo_de_pago
    cliente.fecha_nac = fecha_nac
    cliente.save()

    return redirect("clientes")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")
