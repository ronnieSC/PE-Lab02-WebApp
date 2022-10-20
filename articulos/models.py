from django.db import models
from django.urls import reverse
from categorias.models import Categoria
from ingresos.models import Ingreso_Cabecera
from salidas.models import Salida_Cabecera
from presentaciones.models import Presentacion

# Create your models here.
class Articulo(models.Model):
	ArtCod		= models.CharField(verbose_name='Código del artículo', max_length=15, primary_key=True)
	ArtNom		= models.CharField(verbose_name='Nombre', max_length=30)
	ArtDes		= models.CharField(verbose_name='Descripción', max_length=100, blank=True, null=True)
	ArtImg		= models.ImageField(verbose_name='Imagen', upload_to='pics/articles', blank=True, null=True)
	ArtCatCod	= models.ForeignKey(Categoria, verbose_name='Categoría', on_delete=models.CASCADE)
	ArtCosUni	= models.DecimalField(verbose_name='Costo unitario', max_digits=5, decimal_places=2)
	ArtSitAct	= models.BooleanField(verbose_name='Disponible', default=True)
	ArtSto		= models.IntegerField(verbose_name='Cantidad en stock', default=1)

	ArtIngDet	= models.ManyToManyField(Ingreso_Cabecera, through='Ingreso_Detalle')
	ArtSalDet	= models.ManyToManyField(Salida_Cabecera, through='Salida_Detalle')

	def __str__(self):
		return self.ArtNom
	def get_absolute_url(self):
		return reverse('Editar_Articulo',kwargs={'pk': self.ArtCod})

class Ingreso_Detalle(models.Model):
	class Meta:
		verbose_name_plural = 'Detalle de ingresos de productos'
		unique_together= (('IngDetCabCod', 'IngDetArtCod'),)

	IngDetCabCod	= models.ForeignKey(Ingreso_Cabecera, verbose_name='Código de documento de ingreso', on_delete=models.CASCADE)
	IngDetArtCod	= models.ForeignKey(Articulo, verbose_name='Artículo ingresado', on_delete=models.CASCADE)
	IngDetPreCod	= models.ForeignKey(Presentacion, verbose_name='Presentación del artículo', on_delete=models.CASCADE)
	IngDetCan		= models.IntegerField(verbose_name='Cantidad')
	IngDetCosUni	= models.DecimalField(verbose_name='Costo unitario', max_digits=10, decimal_places=2)

	def __str__(self):
		return 'Artículo ' + self.IngDetArtCod.ArtNom + ' ingresado'

	@property
	def sumarStock(self):
		suma = self.IngDetCan + self.IngDetArtCod.ArtSto
		print(suma)

		return suma

	def save(self):
		articulo = Articulo.objects.get(ArtCod=self.IngDetArtCod.ArtCod)
		articulo.ArtSto = self.sumarStock
		articulo.save()

		super (Ingreso_Detalle, self).save()

class Salida_Detalle(models.Model):
	class Meta:
		unique_together = (('SalDetCabCod', 'SalDetArtCod'),)
		verbose_name_plural = 'Detalles de salida de productos'

	SalDetCabCod	= models.ForeignKey(Salida_Cabecera, verbose_name='Número de factura', on_delete=models.CASCADE)
	SalDetArtCod	= models.ForeignKey(Articulo, verbose_name='Artículo', on_delete=models.CASCADE)
	SalDetPreCod	= models.ForeignKey(Presentacion, verbose_name='Unidad de medida', on_delete=models.CASCADE)
	SalDetCosUni	= models.DecimalField(verbose_name='Costo unitario', max_digits=10, decimal_places=2)
	SalDetCan		= models.IntegerField(verbose_name='Cantidad')

	def __str__(self):
		return str(self.SalDetCabCod) + '-' + str(self.SalDetArtCod)

	@property
	def restarStock(self):
		resta = 0

		if self.SalDetCan < self.SalDetArtCod.ArtSto:
			resta = self.SalDetArtCod.ArtSto - self.SalDetCan

		return resta

	def save(self):
		articulo = Articulo.objects.get(ArtCod=self.SalDetArtCod.ArtCod)
		articulo.ArtSto = self.restarStock
		articulo.save()

		super (Salida_Detalle, self).save()

