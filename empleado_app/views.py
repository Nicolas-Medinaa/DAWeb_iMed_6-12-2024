from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.
def empleados(request):
    losempleados = Empleado.objects.all()
    return render(request, 'gestionarEmpleados.html', {"misempleados": losempleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    cargo = request.POST["txtcargo"]
    correoelectronico = request.POST["txtcorreoelectronico"]
    telefono = request.POST["numtelefono"]
    fechacontratacion = request.POST["datefechacontratacion"]

    guardarEmpleado = Empleado.objects.create(
        id_empleado = id_empleado,
        nombre = nombre,
        cargo = cargo,
        correoelectronico = correoelectronico,
        telefono = telefono,
        fechacontratacion = fechacontratacion
    ) 
    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleados.html", {"misempleados": empleado})

def editarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    cargo = request.POST["txtcargo"]
    correoelectronico = request.POST["txtcorreoelectronico"]
    telefono = request.POST["numtelefono"]
    fechacontratacion = request.POST["datefechacontratacion"]
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.cargo = cargo
    empleado.correoelectronico = correoelectronico
    empleado.telefono = telefono
    empleado.fechacontratacion = fechacontratacion

    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleados")
