from django.shortcuts import render, redirect
from .models import Celular
# Create your views here.
def index(request):
    return render(request, 'index.html')

def celular(request):
    loscelulares=Celular.objects.all()
    return render(request,'gestionarCelulares.html',{"miscelulares":loscelulares})

def registrarCelular(request):
    id_celular=request.POST["txtid"]
    marca=request.POST["txtmarca"]
    modelo=request.POST["txtmodelo"]
    gama=request.POST["txtgama"]
    precios=request.POST["numprecio"]
    idproveedor=request.POST["numidproveedor"]
    idinventario=request.POST["numidinventario"]

   



    guardarCelular=Celular.objects.create(
        id_celular=id_celular,
        marca=marca,
        modelo=modelo,
        gama=gama,
        precios=precios,
        idproveedor=idproveedor,
        idinventario=idinventario
        
    ) 
    return redirect ("celular")

def seleccionarCelular(request,id_celular):
    celular=Celular.objects.get(id_celular=id_celular)
    return render(request,"editarCelulares.html",{"miscelulares":celular})


def editarCelular(request):
    id_celular=request.POST["txtid"]
    marca=request.POST["txtmarca"]
    modelo=request.POST["txtmodelo"]
    gama=request.POST["txtgama"]
    precios=request.POST["numprecio"]
    idproveedor=request.POST["numidproveedor"]
    idinventario=request.POST["numidinventario"]


    celular=Celular.objects.get(id_celular=id_celular)

    celular.id_celular=id_celular
    celular.marca=marca
    celular.modelo=modelo
    celular.gama=gama
    celular.precios=precios
    celular.idproveedor=idproveedor
    celular.idinventario=idinventario
   
    celular.save()
    return redirect("celular") #dsf


def borrarCelular(request,id_celular):
    celular=Celular.objects.get(id_celular=id_celular)
    celular.delete()
    return redirect("celular") #asdsda
