# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150405_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('worker_id', models.CharField(max_length=200)),
                ('assignment_date', models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 54, 57, 575910))),
                ('last_update', models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 54, 57, 575910))),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 54, 57, 574409)),
        ),
        migrations.AddField(
            model_name='taskassignment',
            name='task',
            field=models.ForeignKey(to='website.Task'),
        ),
    ]
