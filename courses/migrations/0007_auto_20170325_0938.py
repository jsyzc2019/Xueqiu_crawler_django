# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20170325_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
