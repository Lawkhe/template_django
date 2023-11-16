from django.db import models

class Temperatura(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    value = models.CharField(max_length=90)

    def __str__(self):
        return self.value