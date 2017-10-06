# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
