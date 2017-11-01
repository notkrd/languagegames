# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lrule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_in', models.CharField(max_length=200)),
                ('str_out', models.CharField(max_length=200)),
                ('rule_priority', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lsystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='lrule',
            name='lsys',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lindenmayergardens.Lsystem'),
        ),
    ]
