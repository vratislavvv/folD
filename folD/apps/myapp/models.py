from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from models_data import *

        
class Bank(models.Model):
    username = models.CharField(max_length=32, unique=True, null=True)

    def __str__(self):
        return str(self.username)


class BankEvent(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bankevent_amount = models.DecimalField(max_digits=20, decimal_places=2)
    bankevent_place = models.CharField(max_length=100)
    bankevent_place_type = models.CharField(max_length=100, choices=PLACE_TYPES)
    bankevent_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.bankevent_amount} at {self.bankevent_place} ({self.bankevent_place_type}) on {self.bankevent_time}"


class Income(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    income_place = models.CharField(max_length=100)
    income_amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
        ]
    )
    income_wageday = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=31),
        ]
    )

    def __str__(self):
        return f"+{self.income_amount}$ from {self.income_place} on {self.income_wageday}."


class Saving(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    saving_amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"+{self.saving_amount}$ to Savings"


class Investment(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    investment_amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"+{self.investment_amount}$ to Investments"
    

class Subscribtion(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    subscribtion_place = models.CharField(max_length=100)
    subscribtion_place_type = models.CharField(max_length=100, choices=PLACE_TYPES)
    subscribtion_repetition = models.IntegerField(choices=PERIOD)
    subscribtion_amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
        ]
    )

    def __str__(self):
        return f"-{self.subscribtion_amount}$ charged every {self.subscribtion_repetition} days"
