from django.db import models

# Create your models here.
class Elemento(models.Model):
    nombre = models.CharField(max_length=90)
    image = models.FileField(upload_to='elementos/',null=True,)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre