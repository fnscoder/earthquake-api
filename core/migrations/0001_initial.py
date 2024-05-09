# Generated by Django 5.0.6 on 2024-05-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("long", models.DecimalField(decimal_places=6, max_digits=9)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "city",
                "verbose_name_plural": "cities",
            },
        ),
    ]
