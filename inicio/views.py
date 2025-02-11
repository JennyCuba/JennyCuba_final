from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

def bienvenida(request):
    return HttpResponse ('<h1>Bienvenida!<h1/>')

def fecha_y_hora(request):
    fecha_y_hora = datetime.now()
    return HttpResponse (f'<h1>esta vista muestra la fecha y hora<h1/>\n{fecha_y_hora}')

def saludo(request, nombre, apellido):
    nombre_formateado = nombre.title()
    apellido_formateado = apellido.title()
    return HttpResponse(f"Buenas {nombre_formateado} {apellido_formateado}, como va?")

def mi_template(request):
    
# V1
    #archivo_abierto = open('Templates\mi_template.html')
    #template = Template(archivo_abierto.read())
    #archivo_abierto.close()
    
    #contexto = Context({'Nombre': 'Jenny'})
    #template_renderizado = template.render(contexto)

    #return HttpResponse(template_renderizado)
    
# v2 con cargador y shortcuts
    template = loader.get_template('mi_template.html')
    return render(request, 'mi_template.html', {'Nombre': 'Jenny'})


def mi_template2(request):
    
# v1 ejemplo template con cargador
    #template = loader.get_template('mi_template2.html')
    #diccionario = {'Nombre': 'Jenny'}
    #template_renderizado = template.render(diccionario)

    #return HttpResponse(template_renderizado)
# v2 resumida
    template = loader.get_template('mi_template2.html')
    return render(request, 'mi_template2.html')

def condicionales_y_bucles(request):
    
   
    return render(request, 'condicionales_y_bucles.html',  {
        'Nombre': 'Jenny',
        'Mis_elementos': [22],
        'Numeros': list(range(15))
    })