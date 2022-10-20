from django.shortcuts import render
from .models import Trabajador
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    )

# Create your views here.
class TrabajadorDetailView(DetailView):
    model = Trabajador

class TrabajadorListView(ListView):
    model = Trabajador

class TrabajadorCreateView(CreateView):
	model = Trabajador
	fields = [
		'TraNomUsu',
		'TraSex',
		'TraFecNac',
        'TraDNI',
        'TraTel',
		]