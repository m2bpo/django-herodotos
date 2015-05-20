# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herodotos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='action',
            field=models.PositiveIntegerField(verbose_name='action'),
        ),
    ]
