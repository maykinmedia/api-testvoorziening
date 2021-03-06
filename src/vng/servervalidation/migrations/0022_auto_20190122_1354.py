# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0021_auto_20190122_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostmanTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validation_file', models.FileField(upload_to='', verbose_name='/files/uploaded_files')),
                ('log', models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='/files/log')),
                ('test_scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.TestScenario')),
            ],
        ),
        migrations.RemoveField(
            model_name='testscenariourl',
            name='log',
        ),
        migrations.RemoveField(
            model_name='testscenariourl',
            name='validation_file',
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
    ]
