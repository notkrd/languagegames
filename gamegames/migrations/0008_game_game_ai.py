# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamegames', '0007_remove_game_possible_moves'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_ai',
            field=models.TextField(null=True),
        ),
    ]
