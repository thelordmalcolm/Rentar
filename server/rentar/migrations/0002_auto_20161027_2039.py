# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='years_lived',
            field=models.CharField(max_length=250, verbose_name='Years lived in'),
        ),
    ]
