# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '\u4f5c\u8005',
                'verbose_name_plural': '\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('author', models.ForeignKey(to='home_application.Author')),
            ],
            options={
                'verbose_name': '\u4e66\u7c4d',
                'verbose_name_plural': '\u4e66\u7c4d',
            },
        ),
        migrations.CreateModel(
            name='sum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sum1', models.CharField(max_length=32)),
                ('sum2', models.CharField(max_length=32)),
                ('summ', models.CharField(max_length=32)),
            ],
        ),
    ]
