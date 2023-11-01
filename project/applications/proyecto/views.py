from django.shortcuts import render
from .models import Proyecto
from django.contrib.auth.decorators import login_required

@login_required
def projects(request):
    proyectos = Proyecto.objects.all()
    response = {'proyectos': proyectos}       
    return render(request, 'proyectos.html', context=response)