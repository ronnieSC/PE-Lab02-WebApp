from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
class Trabajador(models.Model):
	#TraNomUsu	= models.CharField(verbose_name='Nombre de usuario', max_length=30, primary_key=True)
	TraNomUsu	= models.OneToOneField(User, verbose_name='Nombre de usuario', primary_key=True, on_delete=models.CASCADE)
	#TraNom 		= models.CharField(verbose_name='Nombre de pila', max_length=50)
	#TraApe		= models.CharField(verbose_name='Apellidos', max_length=50)

	Masculino = 'M'
	Femenino = 'F'
	sexo_del_trabajador = [
		(Masculino, 'Masculino'),
		(Femenino, 'Femenino'),
	]

	TraSex		= models.CharField(verbose_name='Sexo del trabajador', max_length=1, choices=sexo_del_trabajador, default=Masculino, null=True, blank=True)

	TraFecNac	= models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
	TraDNI		= models.CharField(verbose_name='DNI', max_length=15, null=True, blank=True, unique=True)
	TraTel		= models.CharField(verbose_name='Teléfono de contacto', max_length=15, null=True, blank=True)
	#TraEma		= models.EmailField(verbose_name='Correo electrónico', max_length=100, null=True, blank=True)
	#TraAcc 		= models.BooleanField(verbose_name='Superusuario', default=False)
	#TraPas		= models.CharField(verbose_name='Password', max_length=20)

	class Meta:
		verbose_name_plural='Trabajadores'

	def get_absolute_url(self):
		return reverse('trabajadores:trabajador-detail', kwargs = {'pk': self.TraNomUsu.id})

	def __str__(self):
		return self.TraNomUsu.first_name + ' ' + self.TraNomUsu.last_name
