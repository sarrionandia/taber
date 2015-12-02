# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='Speaker 1',
            new_name='speaker1',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='Speaker 2',
            new_name='speaker2',
        ),
    ]
