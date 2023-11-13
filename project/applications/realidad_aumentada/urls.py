from django.urls import path
from . import views

urlpatterns = [ 
    path('ra/', views.ra, name="RealidadAumentada"),
]