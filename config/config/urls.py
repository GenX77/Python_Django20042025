from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_usu/', include('gestion_usu.urls')),   # Incluye las URLs de gestion_usu bajo /gestion_usu/
    path('', include('gestion_usuarios.urls')),     # Incluye las URLs de gestion_usuarios en la raíz
]