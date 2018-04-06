# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-06 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordDoes',
            fields=[
                ('the_word', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='word')),
            ],
        ),
        migrations.CreateModel(
            name='NameDoes',
            fields=[
                ('worddoes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='verbthegreatnoun.WordDoes')),
            ],
            bases=('verbthegreatnoun.worddoes',),
        ),
        migrations.CreateModel(
            name='NounPhraseDoes',
            fields=[
                ('worddoes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='verbthegreatnoun.WordDoes')),
                ('noun_type', models.CharField(max_length=100)),
                ('capabilities', models.TextField(verbose_name='verbs a subject knows')),
            ],
            bases=('verbthegreatnoun.worddoes',),
        ),
        migrations.CreateModel(
            name='VerbDoes',
            fields=[
                ('worddoes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='verbthegreatnoun.WordDoes')),
                ('action', models.TextField(verbose_name='code for action')),
            ],
            bases=('verbthegreatnoun.worddoes',),
        ),
        migrations.CreateModel(
            name='LocationDoes',
            fields=[
                ('nounphrasedoes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='verbthegreatnoun.NounPhraseDoes')),
                ('exits', models.ManyToManyField(related_name='_locationdoes_exits_+', to='verbthegreatnoun.LocationDoes')),
                ('names_in', models.ManyToManyField(to='verbthegreatnoun.NameDoes')),
            ],
            bases=('verbthegreatnoun.nounphrasedoes',),
        ),
        migrations.AddField(
            model_name='nounphrasedoes',
            name='individuals',
            field=models.ManyToManyField(to='verbthegreatnoun.NameDoes'),
        ),
    ]
