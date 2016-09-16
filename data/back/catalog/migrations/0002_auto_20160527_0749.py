# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import utils.utils
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to=utils.utils.UploadPath('gallery', 'commodity'), validators=[utils.validators.SizeValidator(2)], verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=utils.utils.UploadPath('gallery/thumbs', 'commodity', suff='thumb'), verbose_name='Thumbnail'),
        ),
    ]