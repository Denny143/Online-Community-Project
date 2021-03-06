# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudioUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_from', models.DateTimeField()),
                ('booked_to', models.DateTimeField()),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calender.Place')),
                ('studio_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach_from', models.DateTimeField()),
                ('teach_to', models.DateTimeField()),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calender.Place')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='studio',
            name='Studio_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calender.StudioUser'),
        ),
        migrations.AddField(
            model_name='studio',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calender.Teacher'),
        ),
        migrations.AddField(
            model_name='studio',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calender.Place'),
        ),
    ]
