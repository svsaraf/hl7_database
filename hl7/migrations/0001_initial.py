# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentEVN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponentIN1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponentMSH',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponentNK1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponentPD1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponentPID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponentPV1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('docid', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='componentpv1',
            name='doc',
            field=models.ForeignKey(to='hl7.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='componentpid',
            name='doc',
            field=models.ForeignKey(to='hl7.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='componentpd1',
            name='doc',
            field=models.ForeignKey(to='hl7.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='componentnk1',
            name='doc',
            field=models.ForeignKey(to='hl7.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='componentmsh',
            name='doc',
            field=models.ForeignKey(to='hl7.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='componentin1',
            name='doc',
            field=models.ForeignKey(to='hl7.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='componentevn',
            name='doc',
            field=models.ForeignKey(to='hl7.Document'),
            preserve_default=True,
        ),
    ]
