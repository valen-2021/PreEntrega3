from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!")

def probando_template(request):

    nombre = "Leandro"
    apellido = "Romero"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }

    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
