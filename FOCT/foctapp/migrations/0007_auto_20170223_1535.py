# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0006_auto_20170223_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mirror',
            name='current_error',
            field=models.ImageField(upload_to='', default='null'),
        ),
    ]
