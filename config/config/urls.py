from django.contrib import admin
from django.urls import path, include  # 👈 importa include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saludo.urls')),  # 👈 añade esta línea para enlazar tu app
]
