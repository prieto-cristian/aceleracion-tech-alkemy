from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    fecha_nacimiento = models.DateField()


class Libro(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    isbn = models.CharField()
    fecha_publicacion = models.DateField()
    escrito_por = models.ForeignKey(Autor, on_delete=CASCADE,related_name="libros")
    paginas = models.IntegerField()