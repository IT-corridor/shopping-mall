# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20160715_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='owner',
            new_name='vendor',
        ),
    ]
