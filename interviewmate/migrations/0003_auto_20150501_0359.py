# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewmate', '0002_auto_20150501_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questioncontent',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.TextField(default='empty content', max_length=1024),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='QuestionContent',
        ),
    ]
