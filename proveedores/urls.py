from django.urls import path

from .views import (
	ProveedorListView,
	ProveedorCreateView,
	ProveedorUpdateView,
	ProveedorDeleteView,
	)

urlpatterns = [
	path("listarProveedor", ProveedorListView.as_view(), name="Listar_Proveedor"),
	path("crearProveedor", ProveedorCreateView.as_view(), name="Crear_Proveedor"),		
	path("<pk>/editar", ProveedorUpdateView.as_view(), name="Editar_Proveedor"),
	path("<pk>/borrar/", ProveedorDeleteView.as_view(), name="Eliminar_Proveedor"),
	]