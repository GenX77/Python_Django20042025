<<<<<<< HEAD
from django.urls import path 
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('appointments', AppointmentViewset, basename='appointments')
urlpatterns = router.urls
=======
from django.urls import path 
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('appointments', AppointmentViewset, basename='appointments')
urlpatterns = router.urls
>>>>>>> 72ce678392f09cfcd2104b67e6b794cbbfb143bb
