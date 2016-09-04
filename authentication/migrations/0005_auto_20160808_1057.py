# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20160808_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='bio_long',
            field=models.CharField(default=b'default long bio', max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='bio_short',
            field=models.CharField(default=b'default short bio', max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='company',
            field=models.CharField(default=b'default company', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(default=b'firstnameherp', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(default=b'lastnamederp', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
