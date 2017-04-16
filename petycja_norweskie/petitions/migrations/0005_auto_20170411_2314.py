# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-11 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('petitions', '0004_auto_20170410_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='city_label',
            field=models.CharField(default='City', max_length=100, verbose_name='Label for city field'),
        ),
        migrations.AddField(
            model_name='petition',
            name='email_label',
            field=models.CharField(default='E-mail', max_length=100, verbose_name='Label for email field'),
        ),
        migrations.AddField(
            model_name='petition',
            name='first_name_label',
            field=models.CharField(default='First name', max_length=100, verbose_name='Label for first name field'),
        ),
        migrations.AddField(
            model_name='petition',
            name='organization_label',
            field=models.CharField(default='Organization', max_length=100, verbose_name='Label for organization field'),
        ),
        migrations.AddField(
            model_name='petition',
            name='second_name_label',
            field=models.CharField(default='Second name', max_length=100, verbose_name='Label for second name field'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='slug',
            field=models.CharField(help_text='Used to provide friendly name', max_length=50, unique=True,
                                   verbose_name='Slug'),
        ),
    ]
