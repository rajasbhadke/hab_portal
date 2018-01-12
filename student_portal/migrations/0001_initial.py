# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessFeedback',
            fields=[
                ('hostelName', models.CharField(choices=[(b'Barak', b'Barak'), (b'Bramhaputra', b'Bramhaputra'), (b'Dhansiri', b'Dhansiri'), (b'Dibang', b'Dibang'), (b'Dihing', b'Dihing'), (b'Kameng', b'Kameng'), (b'Kapili', b'Kapili'), (b'Lohit', b'Lohit'), (b'Manas', b'Manas'), (b'Siang', b'Siang'), (b'Subansiri', b'Subansiri'), (b'Umiam', b'Umiam')], max_length=255)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('cleanliness', models.CharField(choices=[(1, b'Very Poor'), (2, b'Poor'), (3, b'Average'), (4, b'Neutral'), (5, b'Good'), (6, b'Very Good')], max_length=255, null=True)),
                ('qual_b', models.IntegerField(choices=[(1, b'Very Poor'), (2, b'Poor'), (3, b'Average'), (4, b'Neutral'), (5, b'Good'), (6, b'Very Good')], null=True)),
                ('qual_l', models.IntegerField(choices=[(1, b'Very Poor'), (2, b'Poor'), (3, b'Average'), (4, b'Neutral'), (5, b'Good'), (6, b'Very Good')], null=True)),
                ('qual_d', models.IntegerField(choices=[(1, b'Very Poor'), (2, b'Poor'), (3, b'Average'), (4, b'Neutral'), (5, b'Good'), (6, b'Very Good')], null=True)),
                ('catering', models.IntegerField(choices=[(1, b'Very Poor'), (2, b'Poor'), (3, b'Average'), (4, b'Neutral'), (5, b'Good'), (6, b'Very Good')], null=True)),
                ('filled', models.BooleanField(default=False)),
                ('month', models.IntegerField(default=12)),
                ('year', models.IntegerField(default=2017)),
            ],
            options={
                'verbose_name': 'MessFeedback',
                'verbose_name_plural': 'MessFeedback',
            },
        ),
        migrations.CreateModel(
            name='Opi_calculated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelName', models.CharField(choices=[(b'Barak', b'Barak'), (b'Bramhaputra', b'Bramhaputra'), (b'Dhansiri', b'Dhansiri'), (b'Dibang', b'Dibang'), (b'Dihing', b'Dihing'), (b'Kameng', b'Kameng'), (b'Kapili', b'Kapili'), (b'Lohit', b'Lohit'), (b'Manas', b'Manas'), (b'Siang', b'Siang'), (b'Subansiri', b'Subansiri'), (b'Umiam', b'Umiam')], max_length=255)),
                ('month', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('opi_value', models.IntegerField()),
                ('numberOfSubscriptions', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Opi_calculated',
                'verbose_name_plural': 'Opi_calculated',
            },
        ),
    ]
