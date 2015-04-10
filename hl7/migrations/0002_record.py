# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hl7', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msh_9', models.TextField()),
                ('msh_10', models.TextField()),
                ('msh_11', models.TextField()),
                ('msh_12', models.TextField()),
                ('pid_5', models.TextField()),
                ('pid_11', models.TextField()),
                ('evn_2', models.TextField()),
                ('evn_4', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
