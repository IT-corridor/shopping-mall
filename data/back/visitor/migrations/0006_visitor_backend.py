# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_auto_20160705_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='backend',
            field=models.CharField(default='weixin', max_length=50, verbose_name='Auth backend'),
        ),
    ]
