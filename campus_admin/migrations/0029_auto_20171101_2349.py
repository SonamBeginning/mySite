# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0028_auto_20171101_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acadYear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='campus_admin.Semester')),
                ('courseNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseNo+', to='campus_admin.Courses')),
                ('semesterNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='campus_admin.Semester')),
            ],
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.RemoveField(
            model_name='student',
            name='programId',
        ),
        migrations.AddField(
            model_name='student',
            name='programName',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='offers',
            unique_together=set([('acadYear', 'semesterNo', 'courseNo')]),
        ),
    ]
