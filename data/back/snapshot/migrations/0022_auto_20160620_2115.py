# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snapshot', '0021_auto_20160620_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.Visitor', verbose_name='Visitor'),
        ),
    ]
