# Generated by Django 2.1.5 on 2019-04-07 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Раздел')),
            ],
        ),
        migrations.CreateModel(
            name='TopicsLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_changed', models.DateField()),
                ('primary_topic', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('topics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Topics')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(through='articles.TopicsLogs', to='articles.Topics'),
        ),
    ]
