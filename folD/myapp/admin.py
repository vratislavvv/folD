from django.contrib import admin
from myapp.models import User, Bank, BankEvent, PlaceType

# Register your models here.

admin.site.register(User)
admin.site.register(Bank)
admin.site.register(BankEvent)
admin.site.register(PlaceType)
