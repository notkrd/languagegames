# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamegames', '0002_game_turn_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='draw_state',
            new_name='draw_conditions',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='loss_state',
            new_name='loss_conditions',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='victory_state',
            new_name='victory_conditions',
        ),
        migrations.AddField(
            model_name='game',
            name='is_game_over',
            field=models.IntegerField(choices=[(0, 'IN PROGRESS'), (1, 'VICTORY'), (2, 'DEFEAT'), (3, 'DRAW')], default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='how_to_play',
            field=models.TextField(default='Unknown'),
        ),
    ]