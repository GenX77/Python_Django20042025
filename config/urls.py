# config/config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_usuarios.urls')),  # Asegúrate de que SOLO tengas esta línea para la raíz
    path('gestion_usu/', include('gestion_usu.urls')),  # Incluye las URLs de gestion_usu
]