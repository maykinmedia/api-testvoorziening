# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-10 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0018_scenario_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenario',
            name='tests',
        ),
        migrations.AddField(
            model_name='scenario',
            name='tests',
            field=models.ManyToManyField(to='testsession.ScenarioCase'),
        ),
    ]
