# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-11-14 09:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171113_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_order',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 14, 43, 58, 488224)),
        ),
    ]