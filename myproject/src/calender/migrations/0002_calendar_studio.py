# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='studio',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
