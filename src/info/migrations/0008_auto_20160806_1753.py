# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumefile',
            old_name='resumes',
            new_name='path',
        ),
    ]
