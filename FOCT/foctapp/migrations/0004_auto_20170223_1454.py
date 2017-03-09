# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0003_auto_20170223_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mirror',
            old_name='fjs_number',
            new_name='fsj_number',
        ),
    ]
