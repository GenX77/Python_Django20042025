<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mycalendar.urls'))
]
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mycalendar.urls'))
]
>>>>>>> 72ce678392f09cfcd2104b67e6b794cbbfb143bb
