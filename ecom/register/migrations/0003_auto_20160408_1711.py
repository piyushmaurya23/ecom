# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20160408_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]