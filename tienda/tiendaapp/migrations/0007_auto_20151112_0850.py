# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0006_producto_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Video',
            field=models.CharField(default='1', max_length=300),
        ),
    ]
