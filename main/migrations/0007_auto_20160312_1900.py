# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_blogpost_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='caption',
            field=models.TextField(default=None, max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default=None, max_length=500, null=True, blank=True),
        ),
    ]
