from django.urls import path
from . import views

urlpatterns = [ 
    path('movil/', views.movil, name="Movil"),
    path('movil_sensor/', views.movil_sensor, name="Temperatura"),
    path('movil_sensor_pro/', views.movil_sensor_pro, name="Proximidad"),
]