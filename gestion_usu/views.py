from django.shortcuts import render

def index(request):
    return render(request, 'gestion_usu/index.html')