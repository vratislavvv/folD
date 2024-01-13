from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Bank, BankEvent, Income
from .forms import BankEventForm, AddIncomeForm, AddSavingForm

@login_required(login_url='login')
def dashboard(request):

    curruser = request.user.id
    expenses = BankEvent.objects.filter(bank_id=curruser)
    incomes = Income.objects.filter(bank_id=curruser)

    context = {'expenses': expenses, 'incomes': incomes}
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
        bank_instance = Bank.objects.get(username=request.user.username)

        forms = [form1, form2]

        for form in forms:
            if form.is_valid():
                form.instance.bank_id = bank_instance
                form.save()

        return redirect('dashboard')
        
    else:
        form1 = AddIncomeForm()
        form2 = AddSavingForm()

    context = {'form1': form1, 'form2': form2}
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/incomes.html", context)