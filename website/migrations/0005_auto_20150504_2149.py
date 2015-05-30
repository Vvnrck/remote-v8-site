# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150504_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskassignment',
            name='worker_id',
        ),
        migrations.AddField(
            model_name='taskassignment',
            name='worker',
            field=models.ForeignKey(default=1, to='website.Worker'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 21, 49, 38, 178214)),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='assignment_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 21, 49, 38, 179715)),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 21, 49, 38, 179715)),
        ),
    ]
