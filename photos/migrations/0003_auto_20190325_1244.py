# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20190315_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='editor',
        ),
        migrations.AddField(
            model_name='article',
            name='editor',
            field=models.ManyToManyField(null=True, to='photos.Editor'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='location',
        ),
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]
