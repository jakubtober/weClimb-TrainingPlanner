# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-23 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0003_auto_20180919_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activation_token',
            field=models.CharField(default='', max_length=128),
        ),
    ]
