# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petorganizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='species',
            field=models.CharField(default='cowform', max_length=31),
        ),
    ]
