from django.shortcuts import render, redirect
from .models import Venta
# Create your views here.
def ventas(request):
    lasventas = Venta.objects.all()
    return render(request, 'gestionarVentas.html', {"misventas": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtid"]
    fechaventa = request.POST["datefechaventa"]
    idcliente = request.POST["txtidcliente"]
    idempleado = request.POST["txtidempleado"]
    listaproducto = request.POST["txtlistaproducto"]
    totalventa = request.POST["numtotalventa"]
    cantidad=request.POST["numcantidad"]

    guardarVenta = Venta.objects.create(
        id_venta = id_venta,
        fechaventa = fechaventa,
        idcliente = idcliente,
        idempleado = idempleado,
        listaproducto = listaproducto,
        totalventa = totalventa,
        cantidad=cantidad
    ) 
    return redirect("ventas")

def seleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    return render(request, "editarVentas.html", {"misventas": venta})

def editarVenta(request):
    id_venta = request.POST["txtid"]
    fechaventa = request.POST["datefechaventa"]
    idcliente = request.POST["txtidcliente"]
    idempleado = request.POST["txtidempleado"]
    listaproducto = request.POST["txtlistaproducto"]
    totalventa = request.POST["numtotalventa"]
    cantidad=request.POST["numcantidad"]
    venta = Venta.objects.get(id_venta=id_venta)
    venta.fechaventa = fechaventa
    venta.idcliente = idcliente
    venta.idempleado = idempleado
    venta.listaproducto = listaproducto
    venta.totalventa = totalventa
    venta.cantidad=cantidad
    venta.save()
    return redirect("ventas")

def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("ventas")
