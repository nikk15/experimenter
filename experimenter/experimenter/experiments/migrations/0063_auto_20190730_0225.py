# Generated by Django 2.1.10 on 2019-07-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("experiments", "0062_experiment_is_paused")]

    operations = [
        migrations.AlterField(
            model_name="experiment",
            name="pref_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Firefox Pref Type"),
                    ("boolean", "boolean"),
                    ("integer", "integer"),
                    ("string", "string"),
                    ("json string", "json string"),
                ],
                max_length=255,
                null=True,
            ),
        )
    ]
