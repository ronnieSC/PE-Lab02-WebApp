from django.urls import path
from .import views

urlpatterns = [
    path('send/<myID>/', views.send, name="Enviar Informacion"),
]