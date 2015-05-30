# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150504_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_benchmark',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 22, 57, 58, 367947)),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='assignment_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 22, 57, 58, 369943)),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 22, 57, 58, 369943)),
        ),
    ]
