# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stats',
            new_name='Character_Stats',
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name_plural': 'Characters'},
        ),
        migrations.AlterModelOptions(
            name='character_stats',
            options={'verbose_name_plural': 'Character_Stats'},
        ),
    ]
