# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-21 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0008_textpluginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='name',
            field=models.CharField(default='migrations', max_length=20),
            preserve_default=False,
        ),
    ]
