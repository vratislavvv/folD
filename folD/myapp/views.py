from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Bank, BankEvent
from .forms import BankEventForm

@login_required(login_url='login')
def dashboard(request):

    curruser = request.user.id
    data = BankEvent.objects.filter(bank_id=curruser)

    context = {'data': data}
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
            return redirect('login')

    else:
        form = BankEventForm() 
    
    context = {'form': form}    
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/new_expense.html", context)

@login_required(login_url='login')
def templates(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/templates.html", {})