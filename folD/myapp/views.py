from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello world!")

@login_required(login_url='login')
def dashboard(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/layouts/layout.html", {})

def login(request):
    if request.method == "GET":
        return render(request, "folD/myapp/templates/login.html")
        return LoginView.as_view(template_name="folD/myapp/templates/login.html")(request)
    
    if request.method == "POST":
        return
    