from django.urls import path
from . import views
urlpatterns = [
    path("", views.mostrar_libros),
    path("crear/autor/<nombre>/<fecha_nacimiento>",views.crear_autor),
]