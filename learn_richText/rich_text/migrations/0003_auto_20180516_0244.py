# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rich_text', '0002_auto_20180516_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='bcontent',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
