from django.urls import path
from celular_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("celular",views.celular,name="celular"),
    path("registrarCelular/",views.registrarCelular,name="registrarCelular"),
    path("seleccionarCelular/<id_celular>",views.seleccionarCelular,name="seleccionarCelular"),
    path("editarCelular/",views.editarCelular, name="editarCelular"),
    path("borrarCelular/<id_celular>",views.borrarCelular,name="borrarCelular"),
    
]