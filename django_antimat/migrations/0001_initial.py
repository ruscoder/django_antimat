# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, verbose_name='Word')),
                ('word_normalized', models.CharField(max_length=50, unique=True, verbose_name='Normalized word')),
            ],
            options={
                'verbose_name': 'Mat',
                'verbose_name_plural': 'Mats',
            },
        ),
    ]
