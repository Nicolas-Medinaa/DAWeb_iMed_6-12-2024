from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta=models.IntegerField()
    fechaventa=models.DateField()
    idcliente=models.IntegerField()
    idempleado=models.IntegerField()
    listaproducto= models.TextField(max_length=500)
    totalventa=models.IntegerField()
    cantidad=models.IntegerField()

    





    def __str__(self) -> str:
        return self.fechaventa