# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20160808_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='content_short',
            field=models.TextField(default=None, blank=True),
            preserve_default=True,
        ),
    ]
