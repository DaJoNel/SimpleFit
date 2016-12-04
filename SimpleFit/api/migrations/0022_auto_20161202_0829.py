# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_clientprofile_dietitian'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='trainer_pending',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_pending', to='api.TrainerProfile'),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to='api.TrainerProfile'),
        ),
    ]