from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def mostrar_libros(request):
    """Trae de la DB todos los libros cargados"""
    libros = models.Libro.objects.all()
    if libros:
        return HttpResponse(libros)
    else:
        return HttpResponse("No hay libros disponibles en este momento")
