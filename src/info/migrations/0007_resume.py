# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20160806_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('resume', models.FileField(upload_to=b'resumes/')),
            ],
        ),
    ]
