# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-26 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=256)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Done', 'Done'), ('Activate', 'Activate')], default='Active', max_length=256)),
            ],
        ),
    ]
