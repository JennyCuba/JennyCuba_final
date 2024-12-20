from django.http import HttpResponse
from datetime import datetime

def bienvenida(request):
    return HttpResponse ('<h1>Bienvenida!<h1/>')

def fecha_y_hora(request):
    fecha_y_hora = datetime.now()
    return HttpResponse (f'<h1>esta vista muestra la fecha y hora<h1/>\n{fecha_y_hora}')