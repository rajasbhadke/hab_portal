# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-07 00:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0019_finalpreference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finalpreference',
            old_name='h1',
            new_name='final_hostel',
        ),
    ]