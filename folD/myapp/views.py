from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import datetime

from .models import Bank, BankEvent, Income, Saving, Investment
from .forms import BankEventForm, AddIncomeForm, AddSavingForm, AddInvestmentForm

@login_required(login_url='login')
def dashboard(request):

    curruser = request.user.id
    expenses = BankEvent.objects.filter(bank_id=curruser)
    incomes = Income.objects.filter(bank_id=curruser)
    saved = Saving.objects.filter(bank_id=curruser)
    invested = Investment.objects.filter(bank_id=curruser)

    expensessum = expenses.aggregate(total_amount=Sum('amount'))['total_amount']
    incomessum = incomes.aggregate(total_amount=Sum('amount1'))['total_amount']
    saved = saved.aggregate(total_amount=Sum('amount2'))['total_amount']
    invested = invested.aggregate(total_amount=Sum('amount3'))['total_amount']
    
    if incomessum == None:
        balance = expensessum * -1
    else:
        balance = incomessum - expensessum

    context = {'expenses': expenses, 'expensessum': expensessum, 'incomes': incomes, 'balance': balance, 'saved': saved, 'invested': invested}
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/index.html", context)

@login_required(login_url='login')
def settings(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/settings.html", {})

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