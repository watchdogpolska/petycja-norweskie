# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-12 00:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0003_set_site_domain_and_name'),
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('organizer', models.CharField(help_text='Person or organization responsible for campaign organization',
                                               max_length=250, verbose_name='Organizer')),
                ('site_title', models.CharField(max_length=150, verbose_name='Name')),
                ('site_subtitle', models.CharField(max_length=150, verbose_name='Subtitle')),
                ('site',
                 models.ForeignKey(help_text='Sites used in campaign', on_delete=django.db.models.deletion.CASCADE,
                                   to='sites.Site', verbose_name='Site')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themes.Theme')),
                ('users', models.ManyToManyField(help_text='Users responsive to manage of campaign',
                                                 to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name_plural': 'Campaigns',
                'verbose_name': 'Campaign',
            },
        ),
    ]
