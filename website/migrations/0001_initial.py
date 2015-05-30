# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(unique=True, max_length=100)),
                ('script', models.FileField(upload_to=django.core.files.storage.FileSystemStorage(location='D:\\Programming\\remoteV8Site\\media/scripts'))),
                ('csv_data', models.FileField(upload_to=django.core.files.storage.FileSystemStorage(location='D:\\Programming\\remoteV8Site\\media/csv'))),
                ('result', models.FileField(upload_to=django.core.files.storage.FileSystemStorage(location='D:\\Programming\\remoteV8Site\\media/results'))),
                ('computed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
