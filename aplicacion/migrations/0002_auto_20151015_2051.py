# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='departamento',
            field=models.ForeignKey(to='aplicacion.Departamento'),
        ),
    ]
