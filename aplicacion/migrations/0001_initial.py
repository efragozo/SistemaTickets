# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=15)),
                ('idTipoId', models.IntegerField()),
                ('nombres', models.CharField(max_length=100, blank=True)),
                ('apellidos', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('direccion', models.CharField(max_length=100, blank=True)),
                ('idEstadoCliente', models.IntegerField()),
                ('Telefonos', models.CharField(max_length=100, blank=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomDepartamento', models.CharField(max_length=15)),
                ('Jefe', models.CharField(max_length=15)),
                ('idEstadoDepartamneto', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atributo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('estadoParametro', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalSoporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=100, blank=True)),
                ('apellidos', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('direccion', models.CharField(max_length=100, blank=True)),
                ('idEstadoSoporte', models.IntegerField()),
                ('Telefonos', models.CharField(max_length=100, blank=True)),
                ('idRol', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IdDescripcion', models.IntegerField()),
                ('FechaReportado', models.DateField(auto_now_add=True)),
                ('FechaArreglado', models.DateField(auto_now_add=True)),
                ('idEstadoTicket', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(to='aplicacion.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ValorParametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.CharField(max_length=30)),
                ('orden', models.CharField(max_length=3)),
                ('estadoValorParametro', models.CharField(max_length=1)),
                ('parametro', models.ForeignKey(to='aplicacion.Parametro')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='departamento',
            field=models.ForeignKey(to='aplicacion.departamento'),
        ),
    ]
