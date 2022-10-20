from django.urls import path, include
from .views import (
    TrabajadorListView,
    TrabajadorDetailView,
    TrabajadorCreateView,
    )

app_name = 'trabajadores'
urlpatterns = [
    path('listarTrabajador', TrabajadorListView.as_view(), name='trabajador-list'),
    path('<pk>/', TrabajadorDetailView.as_view(), name='trabajador-detail'),
    path('crearTrabajador', TrabajadorCreateView.as_view(), name='trabajador-create'),
    path('',include('send.urls')),
]
