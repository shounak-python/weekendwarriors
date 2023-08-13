# Generated by Django 4.2.4 on 2023-08-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bulletin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="Title of Bulletin", max_length=100),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "subtitle",
                    models.CharField(help_text="Subtitle of Bulletin", max_length=200),
                ),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="upload/bulletin/")),
            ],
            options={
                "verbose_name_plural": "Bulletin Board",
            },
        ),
    ]