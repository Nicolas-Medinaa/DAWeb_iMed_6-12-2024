from django.shortcuts import render, redirect
from .models import Inventario
# Create your views here.
def inventarios(request):
    losinventarios = Inventario.objects.all()
    return render(request, 'gestionarInventarios.html', {"misinventarios": losinventarios})

def registrarInventario(request):
    idinventario = request.POST["txtidinventario"]
    idempleado = request.POST["numidempleado"]
    idcelular = request.POST["numidcelular"]
    fecha_inventario = request.POST["datefecha_inventario"]
    cantidad_inventario = request.POST["numcantidad_inventario"]

    guardarInventario = Inventario.objects.create(
        idinventario = idinventario,
        idempleado = idempleado,
        idcelular = idcelular,
        fecha_inventario = fecha_inventario,
        cantidad_inventario = cantidad_inventario
    ) 
    return redirect("inventarios")

def seleccionarInventario(request, idinventario):
    inventario = Inventario.objects.get(idinventario=idinventario)
    return render(request, "editarInventarios.html", {"misinventarios": inventario})

def editarInventario(request):
    idinventario = request.POST["txtidinventario"]
    idempleado = request.POST["numidempleado"]
    idcelular = request.POST["numidcelular"]
    fecha_inventario = request.POST["datefecha_inventario"]
    cantidad_inventario = request.POST["numcantidad_inventario"]
    inventario = Inventario.objects.get(idinventario=idinventario)
    inventario.idempleado = idempleado
    inventario.idcelular = idcelular
    inventario.fecha_inventario = fecha_inventario
    inventario.cantidad_inventario = cantidad_inventario

    inventario.save()
    return redirect("inventarios")

def borrarInventario(request, idinventario):
    inventario = Inventario.objects.get(idinventario=idinventario)
    inventario.delete()
    return redirect("inventarios")
