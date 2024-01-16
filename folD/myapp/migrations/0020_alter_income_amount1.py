# Generated by Django 4.2.7 on 2024-01-16 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0019_remove_investment_interest_remove_investment_place3_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="income",
            name="amount1",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=20,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
