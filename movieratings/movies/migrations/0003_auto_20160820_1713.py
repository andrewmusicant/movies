# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160819_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
