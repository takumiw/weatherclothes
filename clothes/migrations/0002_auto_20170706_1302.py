# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='temp',
            field=models.CharField(choices=[('~5', '~5℃'), ('6~10', '6~10℃'), ('11~15', '11~15℃'), ('16~20', '16~20℃'), ('21~25', '21~25℃'), ('26~30', '26~30℃'), ('31~', '31℃~')], max_length=8),
        ),
    ]
