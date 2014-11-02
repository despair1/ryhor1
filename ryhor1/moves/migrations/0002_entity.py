# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('location', models.ForeignKey(related_name=b'entity', to='moves.locations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
