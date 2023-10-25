from django.shortcuts import render
from .models import Contacto

def projects(request):
    response = {}
    if request.method == "POST":
        data = request.POST

        contacto_val = Contacto()
        contacto_val.nombre = data['name']
        contacto_val.email = data['email']
        contacto_val.telefono = data['phone']
        contacto_val.mensaje = data['message']
        contacto_val.save()

    return render(request, 'contactos.html', context=response)
