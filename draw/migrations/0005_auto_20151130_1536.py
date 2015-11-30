# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0004_auto_20151130_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='chair',
            field=models.ForeignKey(blank=True, to='data.Judge', null=True),
        ),
    ]
