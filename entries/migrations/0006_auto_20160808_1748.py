# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_entry_content_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content_short',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
