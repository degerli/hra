# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-16 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_page_types'),
        ('standardpage', '0003_auto_20170510_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPagePageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_type_relationships', to='standardpage.StandardPage')),
                ('page_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='categories.PageType')),
            ],
        ),
    ]
