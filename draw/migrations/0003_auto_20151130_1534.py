# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0002_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='chair',
            field=models.ForeignKey(to='data.Judge', blank=True),
        ),
    ]
