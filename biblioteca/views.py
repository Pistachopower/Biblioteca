from django.shortcuts import render

# Por cada modelo creamos una vista
def libro_list(request):
    
    return render(request, 'biblioteca/libro_list.html',{})


def autores_list(request):
    return render(request, 'biblioteca/autores_list.html',{})


