# gestion_usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('listar/', views.listar_contactos, name='listar_contactos'),
    path('modificar/<int:contacto_id>/', views.modificar_contacto, name='modificar_contacto'),  # Asegúrate de tener esta línea
]