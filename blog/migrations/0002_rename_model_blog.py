# Generated by Django 5.0.1 on 2024-01-27 13:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Model",
            new_name="blog",
        ),
    ]
