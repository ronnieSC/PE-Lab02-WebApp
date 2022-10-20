from django.db import models
from django.urls import reverse

# Create your models here.
class Proveedor(models.Model):
	ProCod		= models.CharField(verbose_name='RUC del proveedor', max_length=30, primary_key=True)
	ProNom		= models.CharField(verbose_name='Nombre del proveedor', max_length=200)
	ProDir		= models.CharField(verbose_name='Dirección', max_length=200, null=True, blank=True)
	ProTel		= models.CharField(verbose_name='Teléfono', max_length=15, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Proveedores'

	def __str__(self):
		return self.ProNom
		
	def get_absolute_url(self):
		return reverse('Editar_Proveedor',kwargs={'pk': self.ProCod})