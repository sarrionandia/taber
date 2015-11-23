# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('institution', models.ForeignKey(to='data.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('institution', models.ForeignKey(to='data.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='speaker',
            name='team',
            field=models.ForeignKey(to='data.Team'),
        ),
        migrations.AddField(
            model_name='debate',
            name='CG',
            field=models.ForeignKey(related_name='CG', to='data.Team'),
        ),
        migrations.AddField(
            model_name='debate',
            name='CO',
            field=models.ForeignKey(related_name='CO', to='data.Team'),
        ),
        migrations.AddField(
            model_name='debate',
            name='OG',
            field=models.ForeignKey(related_name='OG', to='data.Team'),
        ),
        migrations.AddField(
            model_name='debate',
            name='OO',
            field=models.ForeignKey(related_name='OO', to='data.Team'),
        ),
        migrations.AddField(
            model_name='debate',
            name='chair',
            field=models.ForeignKey(to='data.Judge'),
        ),
        migrations.AddField(
            model_name='debate',
            name='venue',
            field=models.ForeignKey(to='data.Venue'),
        ),
    ]
