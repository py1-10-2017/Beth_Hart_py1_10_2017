# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 00:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applogreg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]
