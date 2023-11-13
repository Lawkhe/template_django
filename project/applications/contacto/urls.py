from django.urls import path
from . import views

urlpatterns = [ 
    path('contacts/', views.projects, name="Contactos"),
    path('exitoso/', views.success, name="exitoso"),
]