# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_experience_dates'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='precedence',
            field=models.IntegerField(default=0),
        ),
    ]