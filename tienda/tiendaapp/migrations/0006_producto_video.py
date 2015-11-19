# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0005_auto_20151028_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Video',
            field=models.CharField(default='1', max_length=30),
        ),
    ]
