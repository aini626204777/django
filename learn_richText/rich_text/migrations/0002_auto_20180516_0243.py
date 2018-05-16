# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rich_text', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='bcontent',
            field=models.TextField(),
        ),
    ]
