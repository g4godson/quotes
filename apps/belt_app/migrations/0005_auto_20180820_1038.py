# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-20 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0004_auto_20180817_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='liked_for',
        ),
        migrations.AddField(
            model_name='quote',
            name='liked_user',
            field=models.ManyToManyField(related_name='liked_quotes', to='belt_app.User'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to='belt_app.User'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]