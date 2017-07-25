# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-25 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('user', models.CharField(max_length=32)),
                ('text', models.CharField(max_length=1024)),
            ],
        ),
    ]