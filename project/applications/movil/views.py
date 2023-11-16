from django.shortcuts import render
from .models import Temperatura
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@login_required
def movil(request):
    response = {}
    return render(request, 'dashboard.html', context=response)

@api_view(['POST'])
def movil_sensor(request):
    response = {"status": False}
    status_response = status.HTTP_400_BAD_REQUEST
    data = request.data
    try:

        temperatura_val = Temperatura()
        temperatura_val.value = data['temperatura']
        temperatura_val.save()

        response['status'] = True
        response['data'] = "Juan"
        status_response = status.HTTP_200_OK
        
    except Exception:
        pass
    return Response(response, status=status_response)