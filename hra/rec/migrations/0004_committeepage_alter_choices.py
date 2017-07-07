# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0003_add_listing_and_social_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeepage',
            name='region',
            field=models.CharField(choices=[('east_midlands', 'East Midlands'), ('east_of_england', 'East of England'), ('england', 'England'), ('london', 'London'), ('north_east', 'North East'), ('north_west', 'North West'), ('northern_ireland', 'Northern Ireland'), ('scotland', 'Scotland'), ('south_central', 'South Central'), ('south_east_coast', 'South East Coast'), ('south_west', 'South West'), ('wales', 'Wales'), ('west_midlands', 'West Midlands'), ('yorkshire_and_the_humber', 'Yorkshire & the Humber')], max_length=64, verbose_name='Region/Nation'),
        ),
    ]
