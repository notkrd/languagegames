# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 17:30
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamegames', '0004_auto_20171018_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='fields_to_display',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=None),
        ),
        migrations.AlterField(
            model_name='game',
            name='draw_conditions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_state',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='loss_conditions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='victory_conditions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
    ]
