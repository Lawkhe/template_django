from django.db import models

class Contacto(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    telefono = models.CharField(max_length=90)
    mensaje = models.CharField(max_length=2000)

    def __str__(self):
        return self.nombre