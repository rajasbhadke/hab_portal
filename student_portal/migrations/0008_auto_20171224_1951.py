# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0007_auto_20171223_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='messfeedback',
            name='month_year',
            field=models.CharField(default=b'11_2017', max_length=255),
        ),
        migrations.AddField(
            model_name='preference',
            name='month_year',
            field=models.CharField(default=b'1_2018', max_length=255),
        ),
    ]