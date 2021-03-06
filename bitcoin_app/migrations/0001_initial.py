# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
                ('time', models.DateTimeField(verbose_name='Time')),
            ],
            options={
                'verbose_name': 'Bitcoin',
                'verbose_name_plural': 'Bitcoins',
            },
        ),
    ]
