from django.urls import path
from . import views

urlpatterns = [
    path('', views.libro_list, name='libro_list'),
    path('autores', views.autores_list, name='autores_list'),
    
]
