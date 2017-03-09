# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0004_auto_20170223_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foct',
            name='foct_testimage',
            field=models.ImageField(upload_to='', default='null'),
        ),
        migrations.AlterField(
            model_name='mirror',
            name='current_error',
            field=models.ImageField(upload_to='/foctapp/', default='null'),
        ),
    ]
