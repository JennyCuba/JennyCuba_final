from inicio.views import bienvenida, fecha_y_hora, mi_template, saludo, mi_template2, condicionales_y_bucles, crear_auto, inicio
from django.urls import path

urlpatterns = [
    path('bienvenida/', bienvenida),
    path('saludo/<str:nombre>/<str:apellido>/', saludo),
    path('fecha_y_hora/', fecha_y_hora),
    path('mi_template/', mi_template),
    path('mi_template2/', mi_template2),
    path('condicionales_y_bucles/', condicionales_y_bucles),
    path('crear_auto/<str:marca>/<str:modelo>/<int:anio>/', crear_auto),
]