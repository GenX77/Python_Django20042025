# gestion_usuarios/views.py
from django.shortcuts import render

def hola_mundo(request):
    return render(request, 'gestion_usu/index.html')
