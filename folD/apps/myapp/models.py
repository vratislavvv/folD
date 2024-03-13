from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from .models_data import PLACE_TYPES, PERIOD

        
class Bank(models.Model):
    username = models.CharField(max_length=32, unique=True, null=True)

    def __str__(self):
        return str(self.username)


class BankEvent(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    place = models.CharField(max_length=100)
    place_type = models.CharField(max_length=100, choices=PLACE_TYPES)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.amount} at {self.place} ({self.place_type}) on {self.time}"


class Income(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
        ]
    )
    wageday = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=31),
        ]
    )

    def __str__(self):
        return f"+{self.amount}$ from {self.place} on {self.wageday}."


class Saving(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"+{self.amount}$ to Savings"


class Investment(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.key}"
    

class Subscribtion(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    place_type = models.CharField(max_length=100, choices=PLACE_TYPES)
    repetition = models.IntegerField(choices=PERIOD)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
        ]
    )

    def __str__(self):
        return f"-{self.amount}$ charged every {self.repetition} days"
