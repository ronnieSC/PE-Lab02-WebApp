from django.urls import path, include

from . import views

urlpatterns = [
	path("register", views.register, name="register"),
	path("login", views.login, name="login"),
	path("logout", views.logout, name="logout"),
	path("menu", views.menu, name="menu"),
	path('articulo/', include('articulos.urls')),
	path('categoria/', include('categorias.urls')),
	path('proveedor/', include('proveedores.urls')),
	path('presentacion/', include('presentaciones.urls')),
	path('trabajador/', include('trabajadores.urls')),
	]