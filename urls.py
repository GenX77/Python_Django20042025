from django.contrib import admin
from django.urls import path
from . import views  # Importa las vistas desde el mismo directorio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hola_mundo, name='hola'),  # Define la URL raíz ('') para tu vista
]