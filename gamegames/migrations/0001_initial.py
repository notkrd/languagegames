# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 17:34
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('how_to_play', models.TextField()),
                ('game_state', django.contrib.postgres.fields.jsonb.JSONField()),
                ('victory_state', django.contrib.postgres.fields.jsonb.JSONField()),
                ('loss_state', django.contrib.postgres.fields.jsonb.JSONField()),
                ('draw_state', django.contrib.postgres.fields.jsonb.JSONField()),
                ('possible_moves', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
