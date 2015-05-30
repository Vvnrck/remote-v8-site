# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150413_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('worker_id', models.CharField(max_length=100, unique=True)),
                ('benchmark_result', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 21, 47, 14, 110104)),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='assignment_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 21, 47, 14, 111105)),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 21, 47, 14, 112104)),
        ),
    ]
