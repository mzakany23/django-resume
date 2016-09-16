# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_skill_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='image',
            field=models.ImageField(null=True, upload_to=b'skill-images', blank=True),
            preserve_default=True,
        ),
    ]
