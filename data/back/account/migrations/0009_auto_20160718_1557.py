# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20160715_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='street_no',
            field=models.CharField(default='', max_length=100, verbose_name='Street number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='build_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Building name'),
        ),
    ]