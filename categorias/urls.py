from django.urls import path

from .views import (
	CategoriaListView,
	CategoriaCreateView,
	CategoriaUpdateView,
	CategoriaDeleteView,
	GeneratePDF,
	)

urlpatterns = [
	path("listarCategoria", CategoriaListView.as_view(), name="Listar_Categoria"),
	path("crearCategoria", CategoriaCreateView.as_view(), name="Crear_Categoria"),
	path("<pk>/editar", CategoriaUpdateView.as_view(), name="Editar_Categoria"),
	path("<pk>/borrar/", CategoriaDeleteView.as_view(), name="Eliminar_Categoria"),

	path('pdf', GeneratePDF.as_view())
	]
