# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import URLshortener.models


class Migration(migrations.Migration):

    dependencies = [
        ('URLshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='shortURL',
            field=models.URLField(default=URLshortener.models.create_short_url, unique=True),
        ),
    ]
