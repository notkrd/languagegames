# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-22 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixedwords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='justtext',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='justtext',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
