# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0009_auto_20170301_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mirror',
            name='current_error',
            field=models.ImageField(upload_to=''),
        ),
    ]
