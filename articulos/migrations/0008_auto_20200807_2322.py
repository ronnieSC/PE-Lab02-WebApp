# Generated by Django 3.0.7 on 2020-08-08 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('articulos', '0007_auto_20200807_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='ArtCatCod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categoria'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='ArtCosUni',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Costo unitario'),
        ),
    ]