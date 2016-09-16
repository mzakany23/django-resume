# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_info_resumes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('resumes', models.FilePathField(blank=True, null=True, path=b'/Users/mzakany/Desktop/resume-django1/static/media/resumes')),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='resumes',
        ),
    ]
