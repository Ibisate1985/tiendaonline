# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0003_auto_20151021_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='combustible',
            new_name='Combustible',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='marca',
            new_name='Marca',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='modelo',
            new_name='Modelo',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='Precio',
        ),
        migrations.AddField(
            model_name='producto',
            name='Vendedores',
            field=models.ManyToManyField(to='tiendaapp.Vendedor'),
        ),
    ]
