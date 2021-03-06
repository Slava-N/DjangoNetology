# Generated by Django 2.1.5 on 2019-05-16 22:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20190516_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='playergameinfo',
            name='session_id',
        ),
        migrations.AlterField(
            model_name='playergameinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 22, 16, 21, 220101)),
        ),
        migrations.AddField(
            model_name='playergameinfo',
            name='creator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='game.Player'),
            preserve_default=False,
        ),
    ]
