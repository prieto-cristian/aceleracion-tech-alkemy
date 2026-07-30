from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
infome_meses = {"enero": "Comienzo del anio con 79.000 ventas",
                    "febrero": "Las ventas cayeron un 20%",
                    "marzo": "Las ventas cayeron 5%",
                    "abril": "Aumento del 50% en el volumen de ventas"}


def hola_mundo(request):
    return HttpResponse("HOLA MUNDO DESDE VIEWS.PY")


def mostrar_informes(request, mes):
    return HttpResponse(infome_meses[mes])