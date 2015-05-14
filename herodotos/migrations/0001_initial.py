# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date')),
                ('action', models.PositiveIntegerField(max_length=20, verbose_name='action')),
                ('comment', models.TextField(verbose_name='comment', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(related_name='history', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date',),
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
