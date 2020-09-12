# Generated by Django 3.1.1 on 2020-09-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("package_monitor", "0007_add_django_version_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="packageversion",
            name="supports_py3",
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text="Does this package support Python3?",
                null=True,
            ),
        ),
    ]