from django.shortcuts import render
from .models import Elemento
from django.contrib.auth.decorators import login_required
import random

@login_required
def ra(request):
    elementos = list(Elemento.objects.all())
    random_elemento = random.choice(elementos)
    response = {'elemento': random_elemento}
    return render(request, 'ra.html', context=response)