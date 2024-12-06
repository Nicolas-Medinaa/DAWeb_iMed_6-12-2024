from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes",views.clientes,name="clientes"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<id_celular>",views.seleccionarCliente,name="seleccionarCliente"),
    path("editarCliente/",views.editarCliente, name="editarCliente"),
    path("borrarCliente/<id_celular>",views.borrarCliente,name="borrarCliente"),
    
]