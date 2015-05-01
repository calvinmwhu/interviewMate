# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewmate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionContent',
            fields=[
                ('question', models.OneToOneField(primary_key=True, serialize=False, to='interviewmate.Question')),
                ('content', models.TextField(max_length=1024)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
    ]
