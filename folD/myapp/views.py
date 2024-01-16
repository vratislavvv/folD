from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db import models
from datetime import datetime

from .models import Bank, BankEvent, Income, Saving, Investment
from .forms import BankEventForm, AddIncomeForm, AddSavingForm, AddInvestmentForm

buffer = 0

@login_required(login_url='login')
def dashboard(request):

    datecheck(request)

    curruser = request.user.id
    expenses = BankEvent.objects.filter(bank_id=curruser)
    incomes = Income.objects.filter(bank_id=curruser)
    saved = Saving.objects.filter(bank_id=curruser)
    invested = Investment.objects.filter(bank_id=curruser)

    expensessum = expenses.aggregate(total_amount=Sum('amount'))['total_amount']
    incomessum = incomes.aggregate(total_amount=Sum('amount1'))['total_amount']
    saved = saved.aggregate(total_amount=Sum('amount2'))['total_amount']
    invested = invested.aggregate(total_amount=Sum('amount3'))['total_amount']
    
    expenses_by_type = BankEvent.objects.values('place_type').annotate(total_amount=models.Sum('amount'))

    if incomessum is not None and expensessum is not None:
        balance = incomessum - expensessum
    elif incomessum == None and expensessum is not None:
        balance = -expensessum
    elif expensessum == None:
        balance = incomessum
    else:
        balance = None


    context = {
        'expenses': expenses, 
        'expensessum': expensessum, 
        'incomes': incomes, 
        'balance': balance, 
        'saved': saved, 
        'invested': invested, 
        'expenses_by_type': expenses_by_type,
    }

    return render(request, "/workspaces/gradeproject/folD/myapp/templates/index.html", context)


@login_required(login_url='login')
def add_expense(request):

    if request.method == "POST":
        form = BankEventForm(request.POST)
        
        if form.is_valid():
            bank_instance = Bank.objects.get(username=request.user.username)
            form.instance.bank_id = bank_instance
            form.instance.time = datetime.now()
            form.save()
            return redirect('dashboard')

    else:
        form = BankEventForm() 
    
    context = {'form': form}    
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/new_expense.html", context)


@login_required(login_url='login')
def incomes(request):

    if request.method == "POST":
        form1 = AddIncomeForm(request.POST)
        form2 = AddSavingForm(request.POST)
        form3 = AddInvestmentForm(request.POST)
        bank_instance = Bank.objects.get(username=request.user.username)

        forms = [form1, form2, form3]

        for form in forms:
            if form.is_valid():
                form.instance.bank_id = bank_instance
                form.save()
        
        if 'flush_incomes' in request.POST:
            Income.objects.filter(bank_id=bank_instance).delete()
        elif 'flush_savings' in request.POST:
            Saving.objects.filter(bank_id=bank_instance).delete()
        elif 'flush_investments' in request.POST:
            Investment.objects.filter(bank_id=bank_instance).delete()

        return redirect('dashboard')
        
    else:
        form1 = AddIncomeForm()
        form2 = AddSavingForm()
        form3 = AddInvestmentForm()

    context = {'form1': form1, 'form2': form2, 'form3': form3}
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/incomes.html", context)


@login_required(login_url='login')
def settings(request):

    if request.method == "POST":
        bank_instance = Bank.objects.get(username=request.user.username)

        Saving.objects.filter(bank_id=bank_instance).delete()
        Investment.objects.filter(bank_id=bank_instance).delete()
        Income.objects.filter(bank_id=bank_instance).delete()
        BankEvent.objects.filter(bank_id=bank_instance).delete()

        return redirect('dashboard')

    return render(request, "/workspaces/gradeproject/folD/myapp/templates/settings.html", {})


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

    