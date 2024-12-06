from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.
def proveedores(request):
    losproveedores = Proveedor.objects.all()
    return render(request, 'gestionarProveedores.html', {"misproveedores": losproveedores})

def registrarProveedor(request):
    id_proveedor = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["numtelefono"]
    correoelectronico = request.POST["txtcorreoelectronico"]
    direccion = request.POST["txtdireccion"]
    listasproductos = request.POST["txtlistasproductos"]

    guardarProveedor = Proveedor.objects.create(
        id_proveedor = id_proveedor,
        nombre = nombre,
        telefono = telefono,
        correoelectronico = correoelectronico,
        direccion = direccion,
        listasproductos = listasproductos,
    ) 
    return redirect("proveedores")

def seleccionarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedores.html", {"misproveedores": proveedor})

def editarProveedor(request):
    id_proveedor = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["numtelefono"]
    correoelectronico = request.POST["txtcorreoelectronico"]
    direccion = request.POST["txtdireccion"]
    listasproductos = request.POST["txtlistasproductos"]
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    proveedor.correoelectronico = correoelectronico
    proveedor.direccion = direccion
    proveedor.listasproductos = listasproductos

    proveedor.save()
    return redirect("proveedores")

def borrarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect("proveedores")
