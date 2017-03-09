# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0002_auto_20170215_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foct',
            name='foct_testimage',
            field=models.ImageField(default='null', upload_to='foctapp/'),
        ),
        migrations.AlterField(
            model_name='mirror',
            name='current_error',
            field=models.ImageField(default='null', upload_to='foctapp/'),
        ),
    ]
