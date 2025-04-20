# gestion_usu/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import os

ARCHIVO_USUARIOS = 'gestion_usu/usuarios.txt'
SEPARADOR = ':::'

def leer_usuarios():
    usuarios = []
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    nombre, telefono, email = linea.split(SEPARADOR)
                    usuarios.append({'nombre': nombre, 'telefono': telefono, 'email': email})
    return usuarios

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as f:
        for usuario in usuarios:
            f.write(f"{usuario['nombre']}{SEPARADOR}{usuario['telefono']}{SEPARADOR}{usuario['email']}\n")

def index(request):
    usuarios = leer_usuarios()
    return render(request, 'gestion_usu/index.html', {'usuarios': usuarios})

def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre'].strip()
        telefono = request.POST['telefono'].strip()
        email = request.POST['email'].strip()
        if nombre and telefono and email:
            usuarios = leer_usuarios()
            usuarios.append({'nombre': nombre, 'telefono': telefono, 'email': email})
            guardar_usuarios(usuarios)
            return redirect(reverse('gestion_usu:index'))
        else:
            return render(request, 'gestion_usu/agregar_usuario.html', {'error': 'Todos los campos son obligatorios.'})
    return render(request, 'gestion_usu/agregar_usuario.html')

def buscar_usuarios(request):
    termino = request.GET.get('q', '').strip().lower()
    resultados = []
    if termino:
        usuarios = leer_usuarios()
        for usuario in usuarios:
            if termino in usuario['nombre'].lower() or termino in usuario['telefono'].lower() or termino in usuario['email'].lower():
                resultados.append(usuario)
    return render(request, 'gestion_usu/index.html', {'usuarios': resultados, 'termino_busqueda': termino})

def editar_usuario(request, indice):
    usuarios = leer_usuarios()
    if indice < 0 or indice >= len(usuarios):
        return redirect(reverse('gestion_usu:index'))
    usuario = usuarios[indice]

    if request.method == 'POST':
        nombre = request.POST['nombre'].strip()
        telefono = request.POST['telefono'].strip()
        email = request.POST['email'].strip()
        if nombre and telefono and email:
            usuarios[indice] = {'nombre': nombre, 'telefono': telefono, 'email': email}
            guardar_usuarios(usuarios)
            return redirect(reverse('gestion_usu:index'))
        else:
            return render(request, 'gestion_usu/editar_usuario.html', {'usuario': usuario, 'indice': indice, 'error': 'Todos los campos son obligatorios.'})
    return render(request, 'gestion_usu/editar_usuario.html', {'usuario': usuario, 'indice': indice})

def borrar_usuario(request, indice):
    usuarios = leer_usuarios()
    if indice < 0 or indice >= len(usuarios):
        return redirect(reverse('gestion_usu:index'))
    if request.method == 'POST':
        del usuarios[indice]
        guardar_usuarios(usuarios)
        return redirect(reverse('gestion_usu:index'))
    return render(request, 'gestion_usu/borrar_usuario.html', {'usuario': usuarios[indice], 'indice': indice})