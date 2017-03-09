# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0007_auto_20170223_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='test_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='foct',
            name='test_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mirror',
            name='test_time',
            field=models.DateField(auto_now=True),
        ),
    ]
