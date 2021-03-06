# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import utils.utils
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('snapshot', '0011_auto_20160616_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=utils.utils.UploadPath('mirror/photo', 'title', 'owner'), validators=[utils.validators.SizeValidator(2)], verbose_name='Group avatar'),
        ),
    ]
