# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0002_debate_venue'),
        ('data', '0002_auto_20151202_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debate', models.ForeignKey(to='draw.Debate')),
                ('judges', models.ManyToManyField(to='data.Judge')),
            ],
        ),
    ]
