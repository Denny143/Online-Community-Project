# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 01:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0002_calendar_studio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='calendar',
            new_name='studio_calendar',
        ),
    ]