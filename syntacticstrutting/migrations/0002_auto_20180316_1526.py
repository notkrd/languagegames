# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-16 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syntacticstrutting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyntaxToxen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_str', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='PhraseRule',
        ),
    ]
