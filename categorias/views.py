from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
	View,
	)

from django.template.loader import get_template
from django.http import HttpResponse
from .utils import render_to_pdf

# Create your views here.
class CategoriaListView(ListView):
	model = Categoria

class CategoriaCreateView(CreateView):
	model = Categoria
	fields = [
		'CatCod',
		'CatDes',
		'CatImg',
		]

class CategoriaUpdateView(UpdateView):
	model = Categoria
	fields = [
		'CatCod',
		'CatDes',
		'CatImg',
		]
	template_name_suffix = '_edit'

class CategoriaDeleteView(DeleteView):
	model = Categoria
	success_url = reverse_lazy('Listar_Categoria')
	template_name_suffix = '_delete'

class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('categoria_reporte.html')

		cats = Categoria.objects.all()

		context = {
		'cats': cats,
		}

		html = template.render(context)
		pdf = render_to_pdf('categoria_reporte.html', context)
		if pdf:
			return HttpResponse(pdf, content_type='application/pdf')
		return HttpResponse('Not Found')
