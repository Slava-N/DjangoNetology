# Generated by Django 2.1.5 on 2019-03-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20190328_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BinaryField(default=False),
        ),
    ]
