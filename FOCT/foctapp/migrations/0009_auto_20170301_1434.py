# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0008_auto_20170224_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mirror',
            name='current_error',
            field=models.ImageField(height_field=200, width_field=400, upload_to=''),
        ),
    ]
