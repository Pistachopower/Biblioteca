from django.shortcuts import render
from .models import Libro, Autores

# Por cada modelo creamos una vista
def libro_list(request):
    libro = Libro.objects.all()
    return render(request, 'biblioteca/libro_list.html',{'libro_list':libro})


def autores_list(request):
    autores= Autores.objects.all()
    return render(request, 'biblioteca/autores_list.html',{'autores_list':autores})


