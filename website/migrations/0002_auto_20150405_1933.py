# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='csv_data',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='D:\\Programming\\remoteV8Site\\media/csv'), upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='result',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='D:\\Programming\\remoteV8Site\\media/results'), upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='script',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='D:\\Programming\\remoteV8Site\\media/scripts'), upload_to=''),
            preserve_default=True,
        ),
    ]
