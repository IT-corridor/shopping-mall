# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snapshot', '0039_auto_20160803_2010'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='photostamp',
            unique_together=set([('photo', 'stamp')]),
        ),
    ]