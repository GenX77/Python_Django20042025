# gestion_usuarios/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q

# Lista de palabras prohibidas comunes en español (puedes extenderla)
palabras_prohibidas = [
    'culo', 'pene', 'vagina', 'gilipollas', 'cabrón', 'zorra', 'mierda', 'joder',
    'coño', 'teta', 'polla', 'maricón', 'puta', 'chingar', 'mamón', 'idiota',
    'imbécil', 'estúpido', 'carajo', 'pendejo', 'boludo', 'concha', 'verga',
    'pendeja', 'zorras', 'cabrones', 'gilipollas', 'maricones', 'putas',
    'mamon', 'idiotas', 'imbeciles', 'estupidos', 'carajos', 'pendejos',
    'boludos', 'conchas', 'vergas', 'pendejas'
    # Puedes añadir más palabras a esta lista
]

# Vista para la página de inicio (index)
def index(request):
    return render(request, 'gestion_usuarios/index.html')  # Corregido: antes decía 'gestion_usu/index.html'

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

# Vista para buscar contactos
def buscar_contactos(request):
    termino_busqueda = request.GET.get('q')
    resultados = []
    mensaje_error = None
    encontro_palabra_prohibida = False

    if termino_busqueda:
        termino_lower = termino_busqueda.lower()
        for palabra in palabras_prohibidas:
            if palabra in termino_lower:
                mensaje_error = f"Lo sentimos, el término de búsqueda '{termino_busqueda}' contiene palabras no permitidas."
                encontro_palabra_prohibida = True
                break  # Importante: salimos del bucle al encontrar la primera palabra prohibida

        if not encontro_palabra_prohibida:
            resultados = Contacto.objects.filter(
                Q(nombre__icontains=termino_busqueda) |
                Q(telefono__icontains=termino_busqueda) |
                Q(email__icontains=termino_busqueda)
            )

    contexto = {
        'contactos': resultados,
        'termino_busqueda': termino_busqueda,
        'mensaje_error': mensaje_error,
    }
    return render(request, 'gestion_usuarios/listar_contactos.html', contexto)

# Vista para eliminar un contacto
def eliminar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, pk=contacto_id)
    if request.method == 'POST':
        contacto.delete()
    return redirect('listar_contactos')
