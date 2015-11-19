# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0008_auto_20151112_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(upload_to='tiendaapp/static/media', null=True),
        ),
    ]
