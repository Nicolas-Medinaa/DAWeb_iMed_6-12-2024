from django.db import models

# Create your models here.
class Inventario(models.Model):
    idinventario=models.IntegerField(null=True,blank=True)
    idempleado=models.IntegerField()
    idcelular=models.IntegerField()
    fecha_inventario=models.DateField()
    cantidad_inventario=models.IntegerField()




