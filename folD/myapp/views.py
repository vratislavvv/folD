from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm

# Create your views here.
def home(request):
    return HttpResponse("hello world!")

def dashboard(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/layouts/layout.html", {})
    