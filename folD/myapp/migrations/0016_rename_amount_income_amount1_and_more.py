# Generated by Django 4.2.7 on 2024-01-13 15:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0015_rename_investments_investment_rename_savings_saving"),
    ]

    operations = [
        migrations.RenameField(
            model_name="income",
            old_name="amount",
            new_name="amount1",
        ),
        migrations.RenameField(
            model_name="income",
            old_name="place",
            new_name="place1",
        ),
        migrations.RenameField(
            model_name="investment",
            old_name="amount",
            new_name="amount3",
        ),
        migrations.RenameField(
            model_name="investment",
            old_name="place",
            new_name="place3",
        ),
        migrations.RenameField(
            model_name="saving",
            old_name="amount",
            new_name="amount2",
        ),
        migrations.RenameField(
            model_name="saving",
            old_name="place",
            new_name="place2",
        ),
    ]