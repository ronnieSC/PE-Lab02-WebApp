from django.shortcuts import render
from .models import Ingreso_Cabecera
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    )

# Create your views here.
class Ingreso_CabeceraCreateView(CreateView):
    model = Ingreso_Cabecera

    fields = [
        'IngCabCod',
        'IngCabFec',
        'IngCabProCod',
        ]
    success_url = reverse_lazy('ingreso_articulo_detalle')