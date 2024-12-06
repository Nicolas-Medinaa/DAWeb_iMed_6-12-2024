from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.
def clientes(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarClientes.html',{"misclientes":losclientes})

def registrarCliente(request):
    id_cliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]
    historial = request.POST["txthistorial"]


   



    guardarCliente=Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        apellido=apellido,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        historial=historial,
    ) 
    return redirect ("clientes")

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarClientes.html",{"misclientes":cliente})


def editarCliente(request):
    id_cliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]
    historial = request.POST["txthistorial"]
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.correo=correo
    cliente.telefono=telefono
    cliente.direccion=direccion
    cliente.historial=historial

   
    cliente.save()
    return redirect("clientes") #dsf


def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes") #asdsda
