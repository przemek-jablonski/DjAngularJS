# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20160808_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='visits',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
