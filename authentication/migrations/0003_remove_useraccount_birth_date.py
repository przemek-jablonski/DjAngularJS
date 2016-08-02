# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20160802_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='birth_date',
        ),
    ]
