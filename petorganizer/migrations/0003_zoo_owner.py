# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petorganizer', '0002_animal_species'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoo',
            name='owner',
            field=models.CharField(default='some owner', max_length=31),
        ),
    ]
