# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-09-15 09:22
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('hyd', django.db.models.manager.Manager()),
            ],
        ),
    ]
