# Generated by Django 3.0.7 on 2020-10-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0127_add_changelogs"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="total_enrolled_clients",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
