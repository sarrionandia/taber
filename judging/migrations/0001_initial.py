# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0001_initial'),
        ('data', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chair', models.ForeignKey(related_name='chairing', to='data.Judge')),
                ('debate', models.ForeignKey(to='draw.Debate')),
                ('judges', models.ManyToManyField(to='data.Judge')),
            ],
        ),
    ]
