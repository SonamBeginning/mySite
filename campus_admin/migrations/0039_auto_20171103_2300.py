# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-03 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0038_auto_20171103_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='feereceipt',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feereceipt',
            name='receiptId',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='feereceipt',
            name='studentId',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='feereceipt_studentId', to='campus_admin.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='feereceipt',
            unique_together=set([('acadYear', 'semesterNo', 'studentId')]),
        ),
    ]
