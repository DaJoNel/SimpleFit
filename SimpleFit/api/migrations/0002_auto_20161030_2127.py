# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='services',
        ),
        migrations.AddField(
            model_name='client',
            name='service',
            field=models.CharField(choices=[('trainer', 'trainer'), ('dietitian', 'dietitian'), ('both', 'both'), ('none', 'none')], default='none', max_length=30),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
