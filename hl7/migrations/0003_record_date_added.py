# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hl7', '0002_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 10, 5, 8, 11, 877440, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
