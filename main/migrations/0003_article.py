# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogpost_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
