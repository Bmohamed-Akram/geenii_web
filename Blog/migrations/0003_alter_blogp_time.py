# Generated by Django 3.2.7 on 2021-09-29 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20210928_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogp',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 7, 14, 6, 270293)),
        ),
    ]
