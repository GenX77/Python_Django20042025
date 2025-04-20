from django.contrib import admin
from django.urls import path, include
from gestion_usuarios import views as gestion_usuarios_views
from gestion_usu import views as gestion_usu_views
from hola import views as hola_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_usuarios/', include('gestion_usuarios.urls')),
    path('gestion_usu/', include('gestion_usu.urls')),
    path('', gestion_usuarios_views.index, name='home'), # <- Enlaza la raíz a la vista 'index' de gestion_usuarios
    # path('', config_views.hola_mundo, name='home'), # <- Comenta o elimina esta línea
    path('', include('hola.urls')), # Si tienes URLs en 'hola'
    # ... otras URLs ...
]
