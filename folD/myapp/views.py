from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/index.html", {})

def settings(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/settings.html", {})
    