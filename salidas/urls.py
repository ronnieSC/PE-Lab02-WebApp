from django.urls import path

from .views import (
    Salida_CabeceraCreateView
    )

app_name = 'salidas'
urlpatterns = [
    path('create/', Salida_CabeceraCreateView.as_view(), name='salida_cabecera-create'),
]