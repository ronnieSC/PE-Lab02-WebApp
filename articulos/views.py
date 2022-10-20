from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Articulo, Ingreso_Detalle, Salida_Detalle
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
	View,
	)

from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from django.http import HttpResponse

from categorias.models import Categoria

# Create your views here.
class Ingreso_DetalleCreateView(CreateView):
	model = Ingreso_Detalle
	fields = [
		'IngDetCabCod',
		'IngDetArtCod',
		'IngDetPreCod',
		'IngDetCan',
		'IngDetCosUni',
		]

class Salida_DetalleCreateView(CreateView):
	model = Salida_Detalle
	fields = [
		'SalDetCabCod',
		'SalDetArtCod',
		'SalDetPreCod',
		'SalDetCosUni',
		'SalDetCan',
		]

class ArticuloListView(ListView):
	model = Articulo

class ArticuloCreateView(CreateView):
	model = Articulo
	fields = [
			'ArtCod',
			'ArtNom',
			'ArtDes',
			'ArtImg',
			'ArtCatCod',
			'ArtCosUni',
			'ArtSitAct',
			'ArtSto',
		]

class ArticuloUpdateView(UpdateView):
	model = Articulo
	fields = [
			'ArtCod',
			'ArtNom',
			'ArtDes',
			'ArtImg',
			'ArtCatCod',
			'ArtCosUni',
			'ArtSitAct',
			'ArtSto',
		]
	template_name_suffix = '_edit'

class ArticuloDeleteView(DeleteView):
	model = Articulo
	success_url = reverse_lazy('Listar_Articulo')
	template_name_suffix = '_delete'

class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('articulos_reporte.html')

		arts = Articulo.objects.all()

		context = {
		'arts': arts,
		}

		html = template.render(context)
		pdf = render_to_pdf('articulos_reporte.html', context)
		if pdf:
			return HttpResponse(pdf, content_type='application/pdf')
		return HttpResponse('Not Found')
