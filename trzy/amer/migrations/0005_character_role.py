# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amer', '0004_auto_20160508_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='role',
            field=models.CharField(choices=[('Mighty squire', 'Mighty squire'), ('Power squire', 'Power squire'), ('Competent Squire', 'Competent Squire'), ('Igor', 'Igor')], default='Mighty squire', max_length=16),
        ),
    ]