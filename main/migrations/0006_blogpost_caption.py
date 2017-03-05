# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_blogpost_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='caption',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
