# gestion_usuarios/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm

# Vista para la página de inicio (index)
def index(request):
    return render(request, 'gestion_usuarios/index.html')

# Vista para listar los contactos
def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'gestion_usuarios/listar_contactos.html', {'contactos': contactos})

# Vista para modificar un contacto
def modificar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, pk=contacto_id)

    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')  # Redirige a la lista de contactos después de guardar
    else:
        form = ContactoForm(instance=contacto)

    return render(request, 'gestion_usuarios/modificar_contacto.html', {'form': form, 'contacto': contacto})

# Vista para agregar un nuevo contacto
def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')  # Redirigir a la lista de contactos después de guardar
    else:
        form = ContactoForm()
    return render(request, 'gestion_usuarios/agregar_contacto.html', {'form': form})