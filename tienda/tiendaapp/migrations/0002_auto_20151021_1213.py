# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('combustible', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
