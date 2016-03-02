# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 22:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('application', '0009_movierequest_user'), ('application', '0010_auto_20160302_2202')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0008_movierequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='movierequest',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
