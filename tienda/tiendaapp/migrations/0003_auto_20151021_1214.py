# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0002_auto_20151021_1213'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
