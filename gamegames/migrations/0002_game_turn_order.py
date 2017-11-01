# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamegames', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='turn_order',
            field=models.IntegerField(choices=[(0, 'SEQUENTIAL'), (1, 'SIMULTANEOUS')], default=0),
        ),
    ]
