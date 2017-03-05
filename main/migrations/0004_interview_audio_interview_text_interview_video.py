# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview_audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interview_text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interview_video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]
