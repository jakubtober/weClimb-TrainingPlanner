# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-19 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_token',
            field=models.CharField(default=uuid.UUID('723e4ef2-fd9b-4380-b3ba-a42912c33094'), max_length=64),
        ),
    ]
