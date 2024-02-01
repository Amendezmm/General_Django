# Generated by Django 4.2.9 on 2024-02-01 02:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("folio", "0004_delete_dbportfolio"),
    ]

    operations = [
        migrations.CreateModel(
            name="dbportfolio",
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
                    "code",
                    models.SlugField(max_length=100, unique=True, verbose_name="Clave"),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "description",
                    models.CharField(max_length=300, verbose_name="Description"),
                ),
                ("url", models.URLField(blank=True, null=True, verbose_name="Link")),
                (
                    "image",
                    models.ImageField(upload_to="static/img", verbose_name="Image"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creation"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
            ],
            options={
                "verbose_name": "Portfolio",
                "verbose_name_plural": "PortFolios",
                "ordering": ["name"],
            },
        ),
    ]