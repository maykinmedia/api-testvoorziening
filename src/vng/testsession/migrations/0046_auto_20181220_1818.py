# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-20 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0045_auto_20181220_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionlog',
            name='request',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='sessionlog',
            name='response',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='vngendpoint',
            name='test_session',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='testsession.TestSession'),
        ),
    ]