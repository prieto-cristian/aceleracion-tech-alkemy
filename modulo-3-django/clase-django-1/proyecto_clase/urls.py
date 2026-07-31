"""
URL configuration for proyecto_clase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def hola_mundo(request):
    return HttpResponse("<h1>HOLA MUNDO</h1>")


def hola_mundo_string(request):
    return  HttpResponse("Hola Mundo como string")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", hola_mundo),
    path("string", hola_mundo_string),
    path("message/", include("informes.urls")),
    path("libreria/", include("libreria.urls"))
]
