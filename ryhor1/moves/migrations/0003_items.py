# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moves', '0002_entity'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('entity', models.ForeignKey(related_name=b'items', to='moves.entity', null=True)),
                ('location', models.ForeignKey(related_name=b'items', to='moves.locations', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
