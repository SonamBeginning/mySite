# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0026_auto_20171101_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acadYear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='campus_admin.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('programId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('programName', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='registers',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='registers',
            name='acadYear',
        ),
        migrations.RemoveField(
            model_name='registers',
            name='courseNo',
        ),
        migrations.RemoveField(
            model_name='registers',
            name='semesterNo',
        ),
        migrations.RemoveField(
            model_name='registers',
            name='studentId',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='acadYear',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='semesterNo',
        ),
        migrations.DeleteModel(
            name='Registers',
        ),
        migrations.AddField(
            model_name='offers',
            name='courseNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseNo+', to='campus_admin.Courses'),
        ),
        migrations.AddField(
            model_name='offers',
            name='semesterNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='student',
            name='programId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programId+', to='campus_admin.Program'),
        ),
        migrations.AlterUniqueTogether(
            name='offers',
            unique_together=set([('acadYear', 'semesterNo', 'courseNo')]),
        ),
    ]
