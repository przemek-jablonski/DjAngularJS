# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_useraccount_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='bio_long',
            field=models.CharField(default=b'long bio', max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='bio_short',
            field=models.CharField(default=b'short bio', max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(default=b'herp', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(default=b'derp', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
