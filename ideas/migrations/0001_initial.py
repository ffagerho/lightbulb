# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('text', models.TextField()),
                ('related', models.ManyToManyField(related_name='_idea_related_+', to='ideas.Idea')),
            ],
        ),
    ]