# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='main_title',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='sub_title',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='last_updated',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
