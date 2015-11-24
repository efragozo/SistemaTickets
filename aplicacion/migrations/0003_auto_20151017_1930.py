# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_auto_20151015_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Telefonos',
            new_name='telefonos',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='Jefe',
            new_name='jefe',
        ),
        migrations.RenameField(
            model_name='personalsoporte',
            old_name='Telefonos',
            new_name='telefonos',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='FechaArreglado',
            new_name='fechaArreglado',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='FechaReportado',
            new_name='fechaReportado',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='IdDescripcion',
            new_name='idDescripcion',
        ),
    ]
