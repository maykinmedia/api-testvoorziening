# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0037_auto_20181218_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExposedUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exposed_url', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsession.Session')),
            ],
        ),
        migrations.RemoveField(
            model_name='vngendpoint',
            name='exposed_api',
        ),
        migrations.AddField(
            model_name='exposedurl',
            name='vng_endpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsession.VNGEndpoint'),
        ),
    ]
