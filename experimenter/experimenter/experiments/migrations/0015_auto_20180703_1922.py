# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("experiments", "0014_auto_20180620_2011")]

    operations = [
        migrations.AlterField(
            model_name="experiment",
            name="firefox_version",
            field=models.CharField(
                choices=[
                    (None, "Firefox Version"),
                    ("55.0", "Firefox 55.0"),
                    ("56.0", "Firefox 56.0"),
                    ("57.0", "Firefox 57.0"),
                    ("58.0", "Firefox 58.0"),
                    ("59.0", "Firefox 59.0"),
                    ("60.0", "Firefox 60.0"),
                    ("61.0", "Firefox 61.0"),
                    ("62.0", "Firefox 62.0"),
                    ("63.0", "Firefox 63.0"),
                    ("64.0", "Firefox 64.0"),
                    ("65.0", "Firefox 65.0"),
                    ("66.0", "Firefox 66.0"),
                    ("67.0", "Firefox 67.0"),
                    ("68.0", "Firefox 68.0"),
                    ("69.0", "Firefox 69.0"),
                    ("70.0", "Firefox 70.0"),
                ],
                max_length=255,
            ),
        )
    ]
