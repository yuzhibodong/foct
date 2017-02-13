# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('phase_error', models.FloatField()),
                ('current_error', models.FloatField()),
                ('light_power', models.FloatField()),
                ('rated_primary_current', models.FloatField()),
                ('ref', models.FloatField()),
                ('composite_error', models.FloatField()),
                ('test_time', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Foct',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('phase_error', models.FloatField()),
                ('current_error', models.FloatField()),
                ('light_power', models.FloatField()),
                ('rated_primary_current', models.FloatField()),
                ('ref', models.FloatField()),
                ('composite_error', models.FloatField()),
                ('test_time', models.DateField()),
                ('max_temperature', models.CharField(max_length=10)),
                ('min_temperature', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='collector',
            name='foct',
            field=models.ForeignKey(to='foctapp.Foct'),
        ),
    ]
