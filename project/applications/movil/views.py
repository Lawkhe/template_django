from django.shortcuts import render
from .models import Temperatura
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

@login_required
def movil(request):
    response = {}

    data_range = [
        [-274, -219],
        [-219, -165],
        [-165, -111],
        [-111, -57],
        [-57, -3],
        [-3, 50],
        [50, 100],
    ]

    labels = ['Menor a -219', 'Menor a -165', 'Menor a -111', 'Menor a -57', 'Menor a -3', 'Menor a 50', 'Mayor a 50']
    data_dashboard = [0,0,0,0,0,0,0]

    temperatura_values = Temperatura.objects.all()

    mint = 100
    maxt = 0
    for tem in temperatura_values:

        mint = mint if mint < int(float(tem.value)) else int(float(tem.value))
        maxt = maxt if maxt > int(float(tem.value)) else int(float(tem.value)) 

        pot = 0
        for ran in data_range:
            if int(float(tem.value)) > ran[0] and int(float(tem.value)) <= ran[1]:
                data_dashboard[pot] += 1
            pot += 1

    total = len(temperatura_values)

    response['labels'] = json.dumps(labels)
    response['data'] = data_dashboard
    response['total'] = total
    response['mint'] = mint
    response['maxt'] = maxt

    return render(request, 'dashboard.html', context=response)

@api_view(['POST'])
def movil_sensor(request):
    response = {'status': False}
    status_response = status.HTTP_400_BAD_REQUEST
    data = request.data
    try:

        temperatura_val = Temperatura()
        temperatura_val.value = data['temperatura']
        temperatura_val.save()

        response['status'] = True
        status_response = status.HTTP_200_OK
        
    except Exception:
        pass
    return Response(response, status=status_response)