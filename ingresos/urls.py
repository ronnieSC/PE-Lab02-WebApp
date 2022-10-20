from django.urls import path

from .views import (
    Ingreso_CabeceraCreateView
    )

app_name = 'ingresos'
urlpatterns = [
    path('create/', Ingreso_CabeceraCreateView.as_view(), name='ingreso_cabecera-create'),
]
