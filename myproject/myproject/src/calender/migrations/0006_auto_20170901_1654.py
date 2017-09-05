# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 20:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0005_auto_20170901_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studioschedule',
            name='Studio_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calender.StudioUser'),
        ),
        migrations.AlterField(
            model_name='studioschedule',
            name='Teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calender.Teacher'),
        ),
        migrations.AlterField(
            model_name='studiouser',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calender.Place'),
        ),
        migrations.AlterField(
            model_name='studiouser',
            name='studio_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
