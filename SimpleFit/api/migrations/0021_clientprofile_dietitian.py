# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_clientprofile_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='dietitian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DietitianProfile'),
        ),
    ]
