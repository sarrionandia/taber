# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20151202_0932'),
        ('draw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='venue',
            field=models.ForeignKey(blank=True, to='data.Venue', null=True),
        ),
    ]
