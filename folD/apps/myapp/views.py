from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.db import models
from datetime import datetime

from .models import Bank, BankEvent, Income, Saving, Investment
from .forms import BankEventForm, AddIncomeForm, AddSavingForm, AddInvestmentForm
from .trading212.trading212api import investment_data

buffer = 0

@login_required(login_url='login')
def dashboard(request):

    # Checking current date
    datecheck(request)

    # Loading data from database into variables
    curruser = request.user.id
    expenses = BankEvent.objects.filter(bank_id=curruser)
    incomes = Income.objects.filter(bank_id=curruser)
    saved = Saving.objects.filter(bank_id=curruser)


    # Trading212 API data loading
    # Trying to access key, later on the account value if the key is correct
    try:
        key = Investment.objects.get(bank_id=curruser)
        key = str(key)
        invested = investment_data(key)

        # This part is here due to unknow errors which occurred while refreshing the page too fast
        if 'invested' in invested and 'ppl' in invested:
            invested = round(invested['invested'], 2) + round(invested['ppl'], 2)
            invested = round(invested, 2)
        else:
            invested = 0

    # If accessing the key wasn't successful, invested amount is set to None
    except ObjectDoesNotExist:
        invested = None
    
    # Summing all expenses, expenses by type, incomes, and saved money
    expensessum = expenses.aggregate(total_amount=Sum('amount'))['total_amount']
    incomessum = incomes.aggregate(total_amount=Sum('amount'))['total_amount']
    saved = saved.aggregate(total_amount=Sum('amount'))['total_amount']
    expenses_by_type = BankEvent.objects.values('place_type').annotate(total_amount=models.Sum('amount')).filter(bank_id=curruser)

    # Creating balance variable which shows total balance 
    if incomessum is not None and expensessum is not None:
        balance = incomessum - expensessum
    elif incomessum == None and expensessum is not None:
        balance = - expensessum
    elif expensessum == None:
        balance = incomessum
    else:
        balance = None

    # Passing context form data
    context = {
        'expenses': expenses, 
        'expensessum': expensessum, 
        'incomes': incomes, 
        'balance': balance, 
        'saved': saved,
        'expenses_by_type': expenses_by_type,
        'invested': invested,
    }
    return render(request, "index.html", context)




@login_required(login_url='login')
def add_expense(request):

    if request.method == "POST":
        form = BankEventForm(request.POST)
        
        if form.is_valid():
            bank_instance = Bank.objects.get(username=request.user.username)
            form.instance.bank = bank_instance
            form.instance.time = datetime.now()
            form.save()
            return redirect('dashboard')

    else:
        form = BankEventForm() 
    
    context = {'form': form}    
    return render(request, "new_expense.html", context)




@login_required(login_url='login')
def incomes(request):

    bank_instance = Bank.objects.get(username=request.user.username)

    if request.method == "POST":
        
        if 'add_income' in request.POST:
            form = AddIncomeForm(request.POST)
            if form.is_valid():
                form.instance.bank = bank_instance
                form.save()

        elif 'add_saving' in request.POST:
            form = AddSavingForm(request.POST)
            if form.is_valid():
                form.instance.bank = bank_instance
                form.save()

        elif 'flush_incomes' in request.POST:
            Income.objects.filter(bank=bank_instance).delete()

        elif 'flush_savings' in request.POST:
            Saving.objects.filter(bank=bank_instance).delete()

        return redirect('dashboard')
        
    else:
        form_income = AddIncomeForm()
        form_saving = AddSavingForm()

    incomes_data = Income.objects.filter(bank=bank_instance)
    savings_data = Saving.objects.filter(bank=bank_instance)

    context = {'form_income': form_income, 'form_saving': form_saving, 'incomes': incomes_data, 'savings': savings_data}
    return render(request, "incomes.html", context)




@login_required(login_url='login')
def settings(request):

    # Gathering form info
    investmentform = AddInvestmentForm()

    # Checking if the method is POST and loading up user nickname
    if request.method == "POST":
        bank_instance = Bank.objects.get(username=request.user.username)
        print(bank_instance)

        # There are 2 POST form on this site
        # Checking for data flushing post form
        if 'flush_data' in request.POST:
            Saving.objects.filter(bank_id=bank_instance).delete()
            Investment.objects.filter(bank_id=bank_instance).delete()
            Income.objects.filter(bank_id=bank_instance).delete()
            BankEvent.objects.filter(bank_id=bank_instance).delete()

        # Checking for investment broker connection
        elif 'submit_api_key' in request.POST:
            api_key_form = AddInvestmentForm(request.POST)

            # If key form is valid, program loads up data and key
            if api_key_form.is_valid():
                api_key = api_key_form.cleaned_data.get('key')
                data = investment_data(api_key)

                # If the key is working
                if type(data) == dict:

                    # If there was a working key before, program removes it
                    try:
                        Investment.objects.get(bank_id=bank_instance)
                        Investment.objects.filter(bank_id=bank_instance).delete()

                    # If first API key, program passes
                    except Investment.DoesNotExist:
                        pass

                    # Saving the key into db
                    api_key_form.instance.bank_id = bank_instance.id
                    api_key_form.instance.key = api_key
                    api_key_form.save()

                    return redirect("dashboard")

                # If the key is not working, application refreshes the page
                else:
                    context = {"error_message": "401: Wrong key"}
                    return redirect("settings")

#                data = investment_data(api_key) {Use this to get data in dashboard view}

    # Passing context form data
    context = {'investmentform': investmentform}
    return render(request, "settings.html", context)




def datecheck(request):
    global buffer

    bank_instance = Bank.objects.get(username=request.user.username)
    wageday = Income.objects.filter(bank_id=bank_instance).first()
    time = datetime.now()
    day = int(time.day)

    if wageday is not None:
        wageday = int(wageday.wageday)

        if day == wageday and buffer == 0:
            buffer += 1
            BankEvent.objects.filter(bank_id=bank_instance).delete()

        elif day != wageday and buffer == 1:
            buffer = 0

    else:
        if day == 1 and buffer == 0:
            buffer += 1
            BankEvent.objects.filter(bank_id=bank_instance).delete()
            return print(11)

        elif day != 1 and buffer == 1:
            buffer = 0

    return 0
