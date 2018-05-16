# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rich_text', '0003_auto_20180516_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='bcontent',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
