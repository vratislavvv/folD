from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return str(self.username)

class Bank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank_account')
    balance = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.balance)

class PlaceType(models.Model):
    place_type = models.CharField(max_length=50)

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
        ('Electronics', 'Electronics'),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
    )

    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    place = models.CharField(max_length=50)
    place_type = models.ForeignKey(PlaceType, on_delete=models.CASCADE)
    time = models.DateField()

    def __str__(self):
        return str(self.amount, self.place, self.place_type, self.time)
