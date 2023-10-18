from django.db import models

# Create your models here.
class Proyecto(models.Model):
    codigo = models.CharField(primary_key=True,max_length=4)
    nombre = models.CharField(max_length=90)
    descripcion = models.CharField( max_length=2000)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return ("On" if self.publish else "Off") + " - " + self.nombre