# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20170822_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='workhistory',
            name='location',
            field=models.CharField(blank=True, max_length=500, verbose_name='location'),
        ),
    ]
