from django.shortcuts import render
from categorias.models import Categoria
from articulos.models import Articulo

# Create your views here.
def index(request):
	categorias = Categoria.objects.all()
	articulos = list(Articulo.objects.all())
	context = {
		'categorias': categorias,
		'articulos': articulos,
	}
	return render(request, 'index.html', context)
