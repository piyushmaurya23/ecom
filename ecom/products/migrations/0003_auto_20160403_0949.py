# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desdription',
            new_name='description',
        ),
    ]