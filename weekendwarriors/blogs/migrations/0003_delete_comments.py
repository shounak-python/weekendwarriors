# Generated by Django 4.2.4 on 2023-08-27 07:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0002_comments"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comments",
        ),
    ]
