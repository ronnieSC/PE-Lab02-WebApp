from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Proveedor
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
	)

# Create your views here.

class ProveedorListView(ListView):
	model = Proveedor

class ProveedorCreateView(CreateView):
	model = Proveedor
	fields = [
		'ProCod',
		'ProNom',
		'ProDir',
        'ProTel',
		]

class ProveedorUpdateView(UpdateView):
	model = Proveedor
	fields = [
		'ProCod',
		'ProNom',
		'ProDir',
        'ProTel',
		]
	template_name_suffix = '_edit'

class ProveedorDeleteView(DeleteView):
	model = Proveedor
	success_url = reverse_lazy('Listar_Proveedor')
	template_name_suffix = '_delete'