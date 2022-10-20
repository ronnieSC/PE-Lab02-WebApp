from django.shortcuts import render
from .models import Salida_Cabecera
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    )

# Create your views here.
class Salida_CabeceraCreateView(CreateView):
    model = Salida_Cabecera

    fields = [
        'SalCabFec',
        ]
    success_url = reverse_lazy('salida_articulo_detalle')