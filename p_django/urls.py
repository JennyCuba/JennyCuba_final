"""
URL configuration for p_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from .views import bienvenida, fecha_y_hora, mi_template, saludo, mi_template2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/', bienvenida),
    path('saludo/<str:nombre>/<str:apellido>/', saludo),
    path('fecha_y_hora/', fecha_y_hora),
    path('mi_template/', mi_template),
    path('mi_template2/', mi_template2),
]

