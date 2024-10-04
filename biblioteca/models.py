from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Libro(models.Model):
    id_libro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo= text = models.TextField()
    id_autor = models.CharField(max_length=200)

class Autores(models.Model):
    id_autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre= text = models.TextField()
    fecha_prestamo = models.DateTimeField(default=timezone.now)