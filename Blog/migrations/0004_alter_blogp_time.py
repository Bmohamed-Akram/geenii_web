# Generated by Django 3.2.7 on 2021-09-29 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_blogp_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogp',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 8, 51, 52, 605983)),
        ),
    ]
