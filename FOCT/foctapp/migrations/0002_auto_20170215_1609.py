# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foctapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mirror',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reflectivity', models.FloatField()),
                ('fsj_lenth', models.FloatField()),
                ('fsj_producter', models.CharField(max_length=20)),
                ('fsj_testproject', models.CharField(max_length=20)),
                ('fsj_recoder', models.CharField(max_length=20)),
                ('fjs_number', models.CharField(max_length=20)),
                ('current_error', models.ImageField(upload_to='image/', default='null')),
                ('test_time', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='foct',
            name='foct_testimage',
            field=models.ImageField(upload_to='image/', default='null'),
        ),
    ]
