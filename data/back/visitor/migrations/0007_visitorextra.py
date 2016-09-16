# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_visitor_backend'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(help_text='4-30 characters, Chinese and English letters, numbers, -, _', max_length=30, unique=True, validators=[utils.validators.validate_weixin], verbose_name='Weixin open id')),
                ('access_token', models.CharField(max_length=255, verbose_name='Weixin Access Token')),
                ('refresh_token', models.CharField(max_length=255, verbose_name='Weixin Refresh Token')),
                ('expires_in', models.PositiveIntegerField(verbose_name='Token expires in')),
                ('token_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Token date')),
                ('backend', models.CharField(default='weixin', max_length=50, verbose_name='Auth backend')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.Visitor', verbose_name='Visitor')),
            ],
            options={
                'verbose_name': 'Extra Data',
            },
        ),
    ]