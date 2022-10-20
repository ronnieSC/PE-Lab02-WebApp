from django.urls import path, include

from .views import (
	ArticuloListView,
	ArticuloCreateView,
	ArticuloUpdateView,
	ArticuloDeleteView,
	Ingreso_DetalleCreateView,
	Salida_DetalleCreateView,
	GeneratePDF
	)

urlpatterns = [
	path("listarArticulo", ArticuloListView.as_view(), name="Listar_Articulo"),
	path("crearArticulo", ArticuloCreateView.as_view(), name="Crear_Articulo"),
	path("<pk>/editar", ArticuloUpdateView.as_view(), name="Editar_Articulo"),
	path("<pk>/borrar/", ArticuloDeleteView.as_view(), name="Eliminar_Articulo"),

	path('ingresar_articulo/', Ingreso_DetalleCreateView.as_view(), name='ingreso_articulo_detalle'),
	path('salir_articulo/', Salida_DetalleCreateView.as_view(), name='salida_articulo_detalle'),
	path('ingresos/', include('ingresos.urls')),
	path('salidas/', include('salidas.urls')),
	path('pdf', GeneratePDF.as_view())
	]
