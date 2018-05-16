# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('gtitle', models.CharField(max_length=23)),
                ('gpic', models.ImageField(upload_to='/static/media')),
                ('isDelete', models.BooleanField(default=False)),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gclick', models.IntegerField(default=0)),
                ('gunit', models.CharField(max_length=20, default='500g')),
                ('gjianjie', models.TextField()),
                ('gpub_date', models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 15, 3, 33, 24, 272992))),
                ('gpubj_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='LeongGoodsApp.TypeInfo'),
        ),
    ]
