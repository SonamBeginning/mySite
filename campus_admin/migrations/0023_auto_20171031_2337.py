# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0022_auto_20171031_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registers',
            name='studentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentId+', to='campus_admin.Student'),
        ),
    ]
