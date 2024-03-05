from django.urls import path, include
from .views import *

urlpatterns = [
    path('cotizaciones/', formularioCotizacion, name="formularioCotizacion"),
] 