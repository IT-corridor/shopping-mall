# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 08:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20160922_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='phone',
            field=utils.fields.CharNullField(blank=True, default=None, max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone must contain 11 numbers, including first "1"', regex='^1\\d{10}$')], verbose_name='Phone'),
        ),
    ]
