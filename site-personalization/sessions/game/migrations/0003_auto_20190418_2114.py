# Generated by Django 2.1.5 on 2019-04-18 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190418_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='finished',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='playergameinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 21, 14, 14, 265342)),
        ),
    ]
