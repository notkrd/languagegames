# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamegames', '0006_move_for_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='possible_moves',
        ),
    ]
