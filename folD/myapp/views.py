from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/index.html", {})

@login_required(login_url='login')
def settings(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/settings.html", {})

@login_required(login_url='login')
def add_expense(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/new_expense.html", {})

@login_required(login_url='login')
def templates(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/templates.html", {})