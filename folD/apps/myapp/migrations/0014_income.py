# Generated by Django 4.2.7 on 2024-01-13 00:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0013_delete_income"),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
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
                ("place", models.CharField(max_length=100)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "wageday",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1),
                            django.core.validators.MaxValueValidator(limit_value=31),
                        ]
                    ),
                ),
                (
                    "bank_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.bank"
                    ),
                ),
            ],
        ),
    ]
