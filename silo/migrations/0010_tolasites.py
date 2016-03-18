# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('silo', '0009_auto_20160120_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='TolaSites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'255', null=True, blank=True)),
                ('agency_name', models.CharField(max_length=b'255', null=True, blank=True)),
                ('agency_url', models.CharField(max_length=b'255', null=True, blank=True)),
                ('privacy_disclaimer', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
        ),
    ]
