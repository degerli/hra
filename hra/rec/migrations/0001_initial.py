# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'committee flag',
                'verbose_name_plural': 'committee flags',
            },
        ),
        migrations.CreateModel(
            name='CommitteeIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CommitteePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('chair', models.CharField(blank=True, max_length=255)),
                ('rec_manager', models.CharField(blank=True, max_length=255, verbose_name='REC Manager')),
                ('rec_assistant', models.CharField(blank=True, max_length=255, verbose_name='REC Assistant')),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('hra_office_name', models.CharField(blank=True, max_length=255, verbose_name='HRA Office name')),
                ('region', models.CharField(choices=[('east_midlands', 'East Midlands'), ('east_of_england', 'East of England'), ('england', 'England'), ('london', 'London'), ('north_east', 'North East'), ('north_west', 'North West'), ('northern_ireland', 'Northern Ireland'), ('scotland', 'Scotland'), ('social_care_institute_for_excellence', 'Social Care Institute for Excellence'), ('south_central', 'South Central'), ('south_east_coast', 'South East Coast'), ('south_west', 'South West'), ('wales', 'Wales'), ('west_midlands', 'West Midlands'), ('yorkshire_and_the_humber', 'Yorkshire & the Humber')], max_length=64, verbose_name='Region/Nation')),
                ('usual_meeting_venue', models.CharField(blank=True, max_length=255)),
                ('usual_meeting_time', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CommitteePageFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('committee_flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rec.CommitteeFlag')),
                ('source_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_flags', to='rec.CommitteePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommitteePageMeetingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('date', models.DateField()),
                ('source_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_dates', to='rec.CommitteePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommitteePagePreviousName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('source_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_names', to='rec.CommitteePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommitteePageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommitteeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'committee type',
                'verbose_name_plural': 'committee types',
            },
        ),
        migrations.AddField(
            model_name='committeepagetype',
            name='committee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rec.CommitteeType'),
        ),
        migrations.AddField(
            model_name='committeepagetype',
            name='source_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_types', to='rec.CommitteePage'),
        ),
    ]
