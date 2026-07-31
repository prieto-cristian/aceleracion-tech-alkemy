from django.urls import path
from . import views


urlpatterns = [
    path("hola-mundo", views.hola_mundo),
    path("<mes>/<int:dia>", views.mostrar_informes),
    path("", views.fecha_actual)
]