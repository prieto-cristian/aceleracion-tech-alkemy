import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
infome_meses = {"enero": "Comienzo del anio con 79.000 ventas",
                    "febrero": "Las ventas cayeron un 20%",
                    "marzo": "Las ventas cayeron 5%",
                    "abril": "Aumento del 50% en el volumen de ventas"}


def hola_mundo(request):
    return HttpResponse("HOLA MUNDO DESDE VIEWS.PY")


def mostrar_informes(request, mes):
    try:
        return HttpResponse(infome_meses[mes])
    except KeyError:
        return HttpResponseNotFound("No hay informes para el mes solicitado")


def fecha_actual(request):
    now = datetime.datetime.now()
    html = "<html lang='es'><body>Fecha actual: %s.</body></html>" % now
    return HttpResponse(html)