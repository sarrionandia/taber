# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0003_auto_20151130_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='venue',
            field=models.ForeignKey(to='data.Venue', blank=True),
        ),
    ]
