# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0004_auto_20151026_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Vendedores',
        ),
        migrations.AddField(
            model_name='producto',
            name='Vendedor',
            field=models.ForeignKey(to='tiendaapp.Vendedor', default=1),
        ),
    ]
