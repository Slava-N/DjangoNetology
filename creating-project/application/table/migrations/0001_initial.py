# Generated by Django 2.1.5 on 2019-04-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Path_to_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choosen_path', models.FilePathField(path='/content_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Table_setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_number', models.IntegerField()),
                ('column_name', models.CharField(max_length=256)),
                ('column_width', models.IntegerField()),
            ],
        ),
    ]
