from django.shortcuts import render
from .models import Proyecto

def projects(request):
    proyectos = Proyecto.objects.all()
    response = {'proyectos': proyectos}       
    return render(request, 'proyectos.html', context=response)