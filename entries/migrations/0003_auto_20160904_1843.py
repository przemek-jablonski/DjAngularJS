# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20160806_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='likes',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='saves',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default=b'Entry title.', max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='visits',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
