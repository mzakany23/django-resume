# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150406_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='link',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
