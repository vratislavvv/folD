from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
        
class Bank(models.Model):
    username = models.CharField(max_length=32, unique=True, null=True)
    balance = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return str(self.username)

class BankEvent(models.Model):
    PLACE_TYPES = (
        ('Groceries', 'Groceries'),
        ('Restaurants', 'Restaurants'),
        ('Cafe', 'Cafe'),
        ('Hobby', 'Hobby'),
        ('Travel', 'Travel'),
        ('Culture', 'Culture'),
        ('Clothing', 'Clothing'),
        ('Subscriptions', 'Subscriptions'),
        ('Telephone, Internet, TV', 'Telephone, Internet, TV'),
        ('Household costs', 'Household costs'),
        ('Household', 'Household'),
        ('Car', 'Car'),
        ('Insurance', 'Insurance'),
        ('Credit card', 'Cradit card'),
        ('Loan', 'Loan'),
        ('Healthcare', 'Healthcare'),
        ('Child', 'Child'),
        ('People', 'People'),
        ('Presents', 'Presents'),
        ('Investments', 'Investments'),
        ('Savings', 'Savings'),
        ('Charity', 'Charity'),
        ('Other', 'Other'),
    )

    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    place = models.CharField(max_length=100)
    place_type = models.CharField(max_length=100, choices=PLACE_TYPES)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.amount} at {self.place} ({self.place_type}) on {self.time}"
