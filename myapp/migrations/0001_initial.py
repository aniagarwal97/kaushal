# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-21 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='resource name')),
                ('bjp', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='myapp.Submission')),
            ],
        ),
    ]