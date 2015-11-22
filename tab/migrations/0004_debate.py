# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tab', '0003_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField()),
                ('CG', models.ForeignKey(related_name='CG', to='tab.Team')),
                ('CO', models.ForeignKey(related_name='CO', to='tab.Team')),
                ('Chair', models.ForeignKey(to='tab.Judge')),
                ('OG', models.ForeignKey(related_name='OG', to='tab.Team')),
                ('OO', models.ForeignKey(related_name='OO', to='tab.Team')),
                ('venue', models.ForeignKey(to='tab.Venue')),
            ],
        ),
    ]
