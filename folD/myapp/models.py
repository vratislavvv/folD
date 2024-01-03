from django.db import models
from django.contrib.auth.models import User
        
class Bank(models.Model):
    username = models.CharField(max_length=32, unique=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.username)

class BankEvent(models.Model):
    PLACE_TYPES = (
        ('Groceries', 'Groceries'),
        ('Restaurants', 'Restaurants'),
        ('Hobby', 'Hobby'),
        ('Investments', 'Investments'),
        ('Charity', 'Charity'),
        ('Savings', 'Savings'),
        ('Travel', 'Travel'),
        ('Healthcare', 'Healthcare'),
        ('Culture', 'Culture'),
        ('Clothing', 'Clothing'),
        ('Household', 'Household'),
        ('Subscriptions', 'Subscriptions'),
        ('Telephone, Internet, TV', 'Telephone, Internet, TV'),
        ('Car', 'Car'),
        ('Child', 'Child'),
        ('Credit card', 'Cradit card'),
        ('Loan', 'Loan'),
        ('Household costs', 'Household costs'),
        ('Insurance', 'Insurance'),
        ('Other', 'Other'),
        ('Presents', 'Presents'),
        ('People', 'People'),
    )

    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    place = models.CharField(max_length=100)
    place_type = models.CharField(max_length=100, choices=PLACE_TYPES)
    time = models.DateField()

    def __str__(self):
        return str(self.amount, self.place, self.place_type, self.time)
