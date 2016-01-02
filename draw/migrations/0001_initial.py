# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('data', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('CG', models.ForeignKey(related_name='CG', to='data.Team')),
                ('CO', models.ForeignKey(related_name='CO', to='data.Team')),
                ('OG', models.ForeignKey(related_name='OG', to='data.Team')),
                ('OO', models.ForeignKey(related_name='OO', to='data.Team')),
                ('venue', models.ForeignKey(blank=True, to='data.Venue', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField()),
            ],
        ),
    ]
