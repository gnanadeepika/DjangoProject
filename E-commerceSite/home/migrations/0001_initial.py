# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-11-09 12:02
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LineDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_of_order', models.DateTimeField(default=datetime.datetime(2017, 11, 9, 17, 32, 15, 820587))),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quanity', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to='')),
                ('description', models.CharField(default=' ', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='linedetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Order'),
        ),
        migrations.AddField(
            model_name='linedetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
    ]
