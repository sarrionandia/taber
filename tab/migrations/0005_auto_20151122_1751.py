# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0004_debate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debate',
            old_name='Chair',
            new_name='chair',
        ),
        migrations.AlterField(
            model_name='debate',
            name='round',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
