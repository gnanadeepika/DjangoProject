# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-11-09 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phoneno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]
