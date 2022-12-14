# Generated by Django 3.0.8 on 2020-07-30 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0002_auto_20200728_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso_Cabecera',
            fields=[
                ('IngCabCod', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Código del documento de ingreso')),
                ('IngCabFec', models.DateField(verbose_name='Fecha de ingreso')),
                ('IngCabProCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'Ingresos',
            },
        ),
    ]
