"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from project.controllers import site
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', site.page),
    path('page/', site.page),
    path('exit/', site.exit, name="exit"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', site.login_view, name="login"),
    path('', include('project.applications.proyecto.urls')),
    path('', include('project.applications.contacto.urls')),
    path('', include('project.applications.ubicaciones.urls')),
    path('', include('project.applications.realidad_aumentada.urls')),
    path('', include('project.applications.movil.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)