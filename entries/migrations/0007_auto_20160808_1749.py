# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_auto_20160808_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content_short',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
