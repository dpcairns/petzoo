# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petorganizer', '0005_auto_20151231_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='pen',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='petorganizer.Pen'),
        ),
        migrations.AddField(
            model_name='pen',
            name='zoo',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='petorganizer.Zoo'),
        ),
    ]
