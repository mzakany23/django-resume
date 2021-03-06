# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 17:00
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='projects')),
            ],
        ),
    ]
