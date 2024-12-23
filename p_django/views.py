from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def bienvenida(request):
    return HttpResponse ('<h1>Bienvenida!<h1/>')

def fecha_y_hora(request):
    fecha_y_hora = datetime.now()
    return HttpResponse (f'<h1>esta vista muestra la fecha y hora<h1/>\n{fecha_y_hora}')

def mi_template(request):
    
# V1
    archivo_abierto = open ('Templates\mi_template.html')
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    
    contexto = Context()
    template_rederizado = template.render(contexto)

    return HttpResponse('template_renderizado')